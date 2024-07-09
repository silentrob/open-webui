<script lang="js">
  import mermaid from 'mermaid';
  import { v4 as uuidv4 } from 'uuid';
  import { getContext, onMount, tick } from 'svelte';
  import { goto } from '$app/navigation';
  import { page } from '$app/stores';
  import { toast } from 'svelte-sonner';
	import { queryMemory } from '$lib/apis/memories';
  import CharacterList from '$lib/components/persona/CharacterList.svelte';
  
  import { createCharacter, getCharacterList } from '$lib/apis/characters/index';
	import { chatCompleted, generateTitle, generateSearchQuery } from '$lib/apis';
  import { getUserSettings } from '$lib/apis/users';
  import { generateChatCompletion } from '$lib/apis/ollama';
  import {
    addTagById,
    createNewChat,
    deleteTagById,
    getAllChatTags,
    getChatById,
    getChatList,
    getTagsById,
    updateChatById
  } from '$lib/apis/chats';

  import {
		convertMessagesToHistory,
		copyToClipboard,
		promptTemplate,
    personaPromptTemplate,
		splitStream
	} from '$lib/utils';

  import {
  chatId,
  chats,
  config,
  models,
  settings,
  showSidebar,
  tags as _tags,
  WEBUI_NAME,
  banners,
  user,
  socket,
  showCallOverlay,
  tools,
} from '$lib/stores';

  import MessageInput from '$lib/components/chat/MessageInput.svelte';
  import PersonaMessages from '$lib/components/persona/PersonaMessages.svelte';
  import Navbar from '$lib/components/layout/Navbar.svelte';
  
  let characters = [];
  let stopResponseFlag = false;
  
  const i18n = getContext('i18n');

  export let chatIdProp = '';
	let loaded = false;

  let title = '';
  let files = [];
  let selectedModels = [''];
  let atSelectedModel = undefined;

  // This is the person we are going to be talking too.
  let selectedCharacter = null;

  let selectedModelIds = [];
  $: selectedModelIds = atSelectedModel !== undefined ? [atSelectedModel.id] : selectedModels;
  let showModelSelector = true;

  let messages = [];
  let selectedToolIds = [];
  let chat = null;
  let prompt = '';
  let processing = '';
  let history = {
      messages: {},
      currentId: null
  };
  let autoScroll = true;
  let messagesContainerElement;


  $: if (history.currentId !== null) {
		let _messages = [];

		let currentMessage = history.messages[history.currentId];
		while (currentMessage !== null) {
			_messages.unshift({ ...currentMessage });
			currentMessage =
				currentMessage.parentId !== null ? history.messages[currentMessage.parentId] : null;
		}
		messages = _messages;
	} else {
		messages = [];
	}

	$: if (chatIdProp) {
		(async () => {
			if (await loadChat()) {
				await tick();
				loaded = true;

				window.setTimeout(() => scrollToBottom(), 0);
				const chatInput = document.getElementById('chat-textarea');
				chatInput?.focus();
			} else {
				await goto('/');
			}
		})();
	}

  const loadChat = async () => {
    chatId.set(chatIdProp);
		chat = await getChatById(localStorage.token, $chatId).catch(async (error) => {
			await goto('/');
			return null;
		});

		if (chat) {
			tags = await getTags();
			const chatContent = chat.chat;

			if (chatContent) {
				console.log(chatContent);

				selectedModels =
					(chatContent?.models ?? undefined) !== undefined
						? chatContent.models
						: [chatContent.models ?? ''];
				history =
					(chatContent?.history ?? undefined) !== undefined
						? chatContent.history
						: convertMessagesToHistory(chatContent.messages);
				title = chatContent.title;

				const userSettings = await getUserSettings(localStorage.token);

				if (userSettings) {
					await settings.set(userSettings.ui);
				} else {
					await settings.set(JSON.parse(localStorage.getItem('settings') ?? '{}'));
				}

				await settings.set({
					...$settings,
					system: chatContent.system ?? $settings.system,
					params: chatContent.options ?? $settings.params
				});

				autoScroll = true;
				await tick();

				if (messages.length > 0) {
					history.messages[messages.at(-1).id].done = true;
				}
				await tick();

				return true;
			} else {
				return null;
			}
		}
	};

  onMount(async () => {

    characters = await getCharacterList();

    if(characters.length > 0) {
      selectedCharacter = characters[0];
    }

		if (!$chatId) {
			await initNewChat();
		} else {
      console.log("Inside else");
			if (!($settings.saveChatHistory ?? true)) {
				await goto('/');
			}
		}
	});

  const initNewChat = async () => {
    window.history.replaceState(history.state, '', `/persona`);
    await chatId.set('');

    autoScroll = true;

    title = '';
    messages = [];
    history = {
      messages: {},
      currentId: null
    };

    if ($page.url.searchParams.get('models')) {
      selectedModels = $page.url.searchParams.get('models')?.split(',');
    } else if ($settings?.models) {
      selectedModels = $settings?.models;
    } else if ($config?.default_models) {
      console.log($config?.default_models.split(',') ?? '');
      selectedModels = $config?.default_models.split(',');
    } else {
      selectedModels = [''];
    }

    selectedModels = selectedModels.map((modelId) =>
      $models.map((m) => m.id).includes(modelId) ? modelId : ''
    );

    const userSettings = await getUserSettings(localStorage.token);

    if (userSettings) {
      settings.set(userSettings.ui);
    } else {
      settings.set(JSON.parse(localStorage.getItem('settings') ?? '{}'));
    }

    const chatInput = document.getElementById('chat-textarea');
    setTimeout(() => chatInput?.focus(), 0);
  };


// This is the main entrypoint for the conversation to start
const submitPrompt = async (userPrompt, _user = null) => {
  
		let _responses = [];
		console.log('submitPrompt', $chatId);

    // Should each character be tied to their own model + settings?
		selectedModels = selectedModels.map((modelId) =>
			$models.map((m) => m.id).includes(modelId) ? modelId : ''
		);

		if (selectedModels.includes('')) {
			toast.error($i18n.t('Model not selected'));
		} else if (messages.length != 0 && messages.at(-1).done != true) {
			// Response not done
			console.log('wait');
		} else if (
			files.length > 0 &&
			files.filter((file) => file.upload_status === false).length > 0
		) {
			// Upload not done
			toast.error(
				$i18n.t(
					`Oops! Hold tight! Your files are still in the processing oven. We're cooking them up to perfection. Please be patient and we'll let you know once they're ready.`
				)
			);
		} else {
			// Reset chat input textarea
			const chatTextAreaElement = document.getElementById('chat-textarea');

			if (chatTextAreaElement) {
				chatTextAreaElement.value = '';
				chatTextAreaElement.style.height = '';
			}

			const _files = JSON.parse(JSON.stringify(files));
			files = [];

			prompt = '';

			// Create user message
			let userMessageId = uuidv4();
			let userMessage = {
				id: userMessageId,
				parentId: messages.length !== 0 ? messages.at(-1).id : null,
				childrenIds: [],
				role: 'user',
				user: _user ?? undefined,
				content: userPrompt,
				files: _files.length > 0 ? _files : undefined,
				timestamp: Math.floor(Date.now() / 1000), // Unix epoch
				models: selectedModels.filter((m, mIdx) => selectedModels.indexOf(m) === mIdx)
			};

			// Add message to history and Set currentId to messageId
			history.messages[userMessageId] = userMessage;
			history.currentId = userMessageId;

			// Append messageId to childrenIds of parent message
			if (messages.length !== 0) {
				history.messages[messages.at(-1).id].childrenIds.push(userMessageId);
			}

			// Wait until history/message have been updated
			await tick();

			// Send prompt
			_responses = await sendPrompt(userPrompt, userMessageId);
		}
		return _responses;
	};


  const sendPrompt = async (prompt, parentId, modelId = null, newChat = true) => {
		let _responses = [];

		// If modelId is provided, use it, else use selected model
		let selectedModelIds = modelId
			? [modelId]
			: atSelectedModel !== undefined
			? [atSelectedModel.id]
			: selectedModels;

		// Create response messages for each selected model
		const responseMessageIds = {};
		for (const modelId of selectedModelIds) {
			const model = $models.filter((m) => m.id === modelId).at(0);

			if (model) {
				let responseMessageId = uuidv4();
				let responseMessage = {
					parentId: parentId,
					id: responseMessageId,
					childrenIds: [],
					role: 'assistant',
					content: '',
					model: model.id,
					modelName: model.name ?? model.id,
					userContext: null,
					timestamp: Math.floor(Date.now() / 1000) // Unix epoch
				};

				// Add message to history and Set currentId to messageId
				history.messages[responseMessageId] = responseMessage;
				history.currentId = responseMessageId;

				// Append messageId to childrenIds of parent message
				if (parentId !== null) {
					history.messages[parentId].childrenIds = [
						...history.messages[parentId].childrenIds,
						responseMessageId
					];
				}

				responseMessageIds[modelId] = responseMessageId;
			}
		}
		await tick();

		// Create new chat if only one message in messages
		if (newChat && messages.length == 2) {
			if ($settings.saveChatHistory ?? true) {
				chat = await createNewChat(localStorage.token, {
					id: $chatId,
					title: `New Chat with ${selectedCharacter?.name}`,
					models: selectedModels,
					system: $settings.system ?? undefined,
					options: {
						...($settings.params ?? {})
					},
					messages: messages,
					history: history,
					tags: [],
					timestamp: Date.now()
				});
				await chats.set(await getChatList(localStorage.token));
				await chatId.set(chat.id);
			} else {
				await chatId.set('local');
			}
			await tick();
		}

		const _chatId = JSON.parse(JSON.stringify($chatId));

		await Promise.all(
			selectedModelIds.map(async (modelId) => {
				const model = $models.filter((m) => m.id === modelId).at(0);

				if (model) {
					// If there are image files, check if model is vision capable
					const hasImages = messages.some((message) =>
						message.files?.some((file) => file.type === 'image')
					);

					if (hasImages && !(model.info?.meta?.capabilities?.vision ?? true)) {
						toast.error(
							$i18n.t('Model {{modelName}} is not vision capable', {
								modelName: model.name ?? model.id
							})
						);
					}

					let responseMessageId = responseMessageIds[modelId];
					let responseMessage = history.messages[responseMessageId];

					let userContext = null;
					if ($settings?.memory ?? false) {
						if (userContext === null) {
							const res = await queryMemory(localStorage.token, prompt).catch((error) => {
								toast.error(error);
								return null;
							});
							if (res) {
								if (res.documents[0].length > 0) {
									userContext = res.documents.reduce((acc, doc, index) => {
										const createdAtTimestamp = res.metadatas[index][0].created_at;
										const createdAtDate = new Date(createdAtTimestamp * 1000)
											.toISOString()
											.split('T')[0];
										acc.push(`${index + 1}. [${createdAtDate}]. ${doc[0]}`);
										return acc;
									}, []);
								}

								console.log(userContext);
							}
						}
					}
					responseMessage.userContext = userContext;

					const chatEventEmitter = await getChatEventEmitter(model.id, _chatId);

					let _response = null;
					if (model?.owned_by === 'openai')  {
            console.log("OPEN AI is not support in persona")
          }		
					_response = await sendPromptOllama(model, prompt, responseMessageId, _chatId);
					_responses.push(_response);

					console.log('chatEventEmitter', chatEventEmitter);

					if (chatEventEmitter) clearInterval(chatEventEmitter);
				} else {
					toast.error($i18n.t(`Model {{modelId}} not found`, { modelId }));
				}
			})
		);

		await chats.set(await getChatList(localStorage.token));

		return _responses;
	};

  const getChatEventEmitter = async (modelId, chatId = '') => {
		return setInterval(() => {
			$socket?.emit('usage', {
				action: 'chat',
				model: modelId,
				chat_id: chatId
			});
		}, 1000);
	};

	const stopResponse = () => {
		stopResponseFlag = true;
		console.log('stopResponse');
	};

	const scrollToBottom = async () => {
		await tick();
		if (messagesContainerElement) {
			messagesContainerElement.scrollTop = messagesContainerElement.scrollHeight;
		}
	};

  const createMessagesList = (responseMessageId) => {
		const message = history.messages[responseMessageId];
		if (message.parentId) {
			return [...createMessagesList(message.parentId), message];
		} else {
			return [message];
		}
	};

  const sendPromptOllama = async (model, userPrompt, responseMessageId, _chatId) => {
		let _response = null;

		const responseMessage = history.messages[responseMessageId];

		// Wait until history/message have been updated
		await tick();

		// Scroll down
		scrollToBottom();
    
		const messagesBody = [
			selectedCharacter?.prompt
				? {
						role: 'system',
						content: `${personaPromptTemplate(selectedCharacter.prompt, selectedCharacter,  $user.name)}`
				  }
				: $settings.system || (responseMessage?.userContext ?? null)
				? {
						role: 'system',
						content: `${promptTemplate($settings?.system ?? '', $user.name)}${
							responseMessage?.userContext ?? null
								? `\n\nUser Context:\n${(responseMessage?.userContext ?? []).join('\n')}`
								: ''
						}`
				  }
				: undefined,
			...messages
		]
			.filter((message) => message?.content?.trim())
			.map((message, idx, arr) => {
				// Prepare the base message object
				const baseMessage = {
					role: message.role,
					content: message.content
				};

				// Extract and format image URLs if any exist
				const imageUrls = message.files
					?.filter((file) => file.type === 'image')
					.map((file) => file.url.slice(file.url.indexOf(',') + 1));

				// Add images array only if it contains elements
				if (imageUrls && imageUrls.length > 0 && message.role === 'user') {
					baseMessage.images = imageUrls;
				}
				return baseMessage;
			});

		let lastImageIndex = -1;

		// Find the index of the last object with images
		messagesBody.forEach((item, index) => {
			if (item.images) {
				lastImageIndex = index;
			}
		});

		// Remove images from all but the last one
		messagesBody.forEach((item, index) => {
			if (index !== lastImageIndex) {
				delete item.images;
			}
		});

		let docs = [];

		if (model?.info?.meta?.knowledge ?? false) {
			docs = model.info.meta.knowledge;
		}

		docs = [
			...docs,
			...messages
				.filter((message) => message?.files ?? null)
				.map((message) =>
					message.files.filter((item) =>
						['doc', 'collection', 'web_search_results'].includes(item.type)
					)
				)
				.flat(1)
		].filter(
			(item, index, array) =>
				array.findIndex((i) => JSON.stringify(i) === JSON.stringify(item)) === index
		);

		const [res, controller] = await generateChatCompletion(localStorage.token, {
			model: model.id,
			messages: messagesBody,
			options: {
				...($settings.params ?? {}),
				stop:
					$settings?.params?.stop ?? undefined
						? $settings.params.stop.map((str) =>
								decodeURIComponent(JSON.parse('"' + str.replace(/\"/g, '\\"') + '"'))
						  )
						: undefined,
				num_predict: $settings?.params?.max_tokens ?? undefined,
				repeat_penalty: $settings?.params?.frequency_penalty ?? undefined
			},
			format: $settings.requestFormat ?? undefined,
			keep_alive: $settings.keepAlive ?? undefined,
			tool_ids: selectedToolIds.length > 0 ? selectedToolIds : undefined,
			docs: docs.length > 0 ? docs : undefined,
			citations: docs.length > 0,
      character_id: selectedCharacter?.id,
			chat_id: $chatId
		});

		if (res && res.ok) {
			console.log('controller', controller);

			const reader = res.body
				.pipeThrough(new TextDecoderStream())
				.pipeThrough(splitStream('\n'))
				.getReader();

			while (true) {
				const { value, done } = await reader.read();
				if (done || stopResponseFlag || _chatId !== $chatId) {
          console.log("Good we stopped!");

					responseMessage.done = true;
					messages = messages;

					if (stopResponseFlag) {
						controller.abort('User: Stop Response');
					} else {
						const messages = createMessagesList(responseMessageId);
						await chatCompletedHandler(model.id, messages);
					}

					_response = responseMessage.content;
					break;
				}

				try {
					let lines = value.split('\n');
					for (const line of lines) {
						if (line !== '') {
							let data = JSON.parse(line);
							if ('citations' in data) {
								responseMessage.citations = data.citations;
								continue;
							}

							if ('detail' in data) {
								throw data;
							}

							if (data.done == false) {
								if (responseMessage.content == '' && data.message.content == '\n') {
									continue;
								} else {
									responseMessage.content += data.message.content;
									messages = messages;
								}
							} else {
								responseMessage.done = true;

								if (responseMessage.content == '') {
									responseMessage.error = {
										code: 400,
										content: `Oops! No text generated from Ollama, Please try again.`
									};
								}

								responseMessage.context = data.context ?? null;
								responseMessage.info = {
									total_duration: data.total_duration,
									load_duration: data.load_duration,
									sample_count: data.sample_count,
									sample_duration: data.sample_duration,
									prompt_eval_count: data.prompt_eval_count,
									prompt_eval_duration: data.prompt_eval_duration,
									eval_count: data.eval_count,
									eval_duration: data.eval_duration
								};
								messages = messages;
							}
						}
					}
				} catch (error) {
					console.log(error);
					if ('detail' in error) {
						toast.error(error.detail);
					}
					break;
				}

				if (autoScroll) {
					scrollToBottom();
				}
			}

			// if ($chatId == _chatId) {
			// 	if ($settings.saveChatHistory ?? true) {
			// 		chat = await updateChatById(localStorage.token, _chatId, {
			// 			messages: messages,
			// 			history: history,
			// 			models: selectedModels
			// 		});
			// 		await chats.set(await getChatList(localStorage.token));
			// 	}
			// }
		} else {
			if (res !== null) {
				const error = await res.json();
				console.log(error);
				if ('detail' in error) {
					toast.error(error.detail);
					responseMessage.error = { content: error.detail };
				} else {
					toast.error(error.error);
					responseMessage.error = { content: error.error };
				}
			} else {
				toast.error(
					$i18n.t(`Uh-oh! There was an issue connecting to {{provider}}.`, { provider: 'Ollama' })
				);
				responseMessage.error = {
					content: $i18n.t(`Uh-oh! There was an issue connecting to {{provider}}.`, {
						provider: 'Ollama'
					})
				};
			}
			responseMessage.done = true;
			messages = messages;
		}

		stopResponseFlag = false;
		await tick();

		if (autoScroll) {
			scrollToBottom();
		}

		return _response;
	};


  const chatCompletedHandler = async (modelId, messages) => {
		await mermaid.run({
			querySelector: '.mermaid'
		});

		const res = await chatCompleted(localStorage.token, {
			model: modelId,
			messages: messages.map((m) => ({
				id: m.id,
				role: m.role,
				content: m.content,
				timestamp: m.timestamp
			})),
			chat_id: $chatId
		}).catch((error) => {
			console.error(error);
			return null;
		});

		if (res !== null) {
			// Update chat history with the new messages
			for (const message of res.messages) {
				history.messages[message.id] = {
					...history.messages[message.id],
					...(history.messages[message.id].content !== message.content
						? { originalContent: history.messages[message.id].content }
						: {}),
					...message
				};
			}
		}
	};

  
  const regenerateResponse = async (message) => {
		console.log('regenerateResponse');

		if (messages.length != 0) {
			let userMessage = history.messages[message.parentId];
			let userPrompt = userMessage.content;

			if ((userMessage?.models ?? [...selectedModels]).length == 1) {
				await sendPrompt(userPrompt, userMessage.id, undefined, false);
			} else {
				await sendPrompt(userPrompt, userMessage.id, message.model, false);
			}
		}
	};

  const continueGeneration = async () => {
		console.log('continueGeneration');
		const _chatId = JSON.parse(JSON.stringify($chatId));

		if (messages.length != 0 && messages.at(-1).done == true) {
			const responseMessage = history.messages[history.currentId];
			responseMessage.done = false;
			await tick();

			const model = $models.filter((m) => m.id === responseMessage.model).at(0);

			if (model) {
				if (model?.owned_by === 'openai') {
					console.log("OPEN AI is not support in persona")
				} else
					await sendPromptOllama(
						model,
						history.messages[responseMessage.parentId].content,
						responseMessage.id,
						_chatId
					);
			}
		} else {
			toast.error($i18n.t(`Model {{modelId}} not found`, { modelId }));
		}
	};

</script>


<div
  class="h-screen max-h-[100dvh] {$showSidebar
      ? 'md:max-w-[calc(100%-260px)]'
      : ''} w-full max-w-full flex flex-col"
  >

  <div class="flex flex-row flex-auto">
      <div class="flex flex-col flex-auto">
            <div class="h-full w-full flex flex-col">
                <Navbar
                    {title}
                    bind:selectedModels
                    bind:showModelSelector
                    shareEnabled={messages.length > 0}
                    {chat}
                    {initNewChat}
                />

                <div
                  class=" pb-2.5 flex flex-col justify-between w-full flex-auto overflow-auto h-0 max-w-full"
                  id="messages-container"
                  bind:this={messagesContainerElement}
                  on:scroll={(e) => {
                    autoScroll =
                      messagesContainerElement.scrollHeight - messagesContainerElement.scrollTop <=
                      messagesContainerElement.clientHeight + 5;
                  }}
                >

                  <div class=" h-full w-full flex flex-col pt-2 pb-4">
                    <!-- Messages component or other content here -->
                    <PersonaMessages
                      chatId={$chatId}
                      {selectedModels}
                      {processing}
                      bind:history
                      bind:messages
                      bind:autoScroll
                      bind:prompt
                      bottomPadding={files.length > 0}
                      {sendPrompt}
                      {continueGeneration}
                      {regenerateResponse}
                    />
                  </div>
                </div>

              <div class="mt-auto">
                  <MessageInput
                    {selectedModels}
                    {messages}
                    {submitPrompt}
                    {stopResponse}
                  />
              </div>
            </div>
        
      </div>
      <div class="w-64 flex-none bg-gray-100 dark:bg-gray-800 p-1">
          <div class="px-1.5 flex justify-center text-gray-800 dark:text-gray-200">
              <a class="flex-grow flex space-x-3 rounded-xl px-2.5 py-2 hover:bg-gray-100 dark:hover:bg-gray-900 transition"
                  href="/character/settings"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-fill-gear" viewBox="0 0 16 16">
                    <path d="M11 5a3 3 0 1 1-6 0 3 3 0 0 1 6 0m-9 8c0 1 1 1 1 1h5.256A4.5 4.5 0 0 1 8 12.5a4.5 4.5 0 0 1 1.544-3.393Q8.844 9.002 8 9c-5 0-6 3-6 4m9.886-3.54c.18-.613 1.048-.613 1.229 0l.043.148a.64.64 0 0 0 .921.382l.136-.074c.561-.306 1.175.308.87.869l-.075.136a.64.64 0 0 0 .382.92l.149.045c.612.18.612 1.048 0 1.229l-.15.043a.64.64 0 0 0-.38.921l.074.136c.305.561-.309 1.175-.87.87l-.136-.075a.64.64 0 0 0-.92.382l-.045.149c-.18.612-1.048.612-1.229 0l-.043-.15a.64.64 0 0 0-.921-.38l-.136.074c-.561.305-1.175-.309-.87-.87l.075-.136a.64.64 0 0 0-.382-.92l-.148-.045c-.613-.18-.613-1.048 0-1.229l.148-.043a.64.64 0 0 0 .382-.921l-.074-.136c-.306-.561.308-1.175.869-.87l.136.075a.64.64 0 0 0 .92-.382zM14 12.5a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0"/>
                </svg>
                <div class="flex self-center">
                    <div class=" self-center font-medium text-sm">Characters</div>
                </div>
              </a>
                <button on:click={createCharacter}>
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
                    <path d="M16 8a8 8 0 1 1-16 0 8 8 0 0 1 16 0zM8 4a.5.5 0 0 0-.5.5v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3A.5.5 0 0 0 8 4z"/>
                  </svg>
                </button>
          </div>

          <CharacterList />
        </div>

      </div>
  </div>


