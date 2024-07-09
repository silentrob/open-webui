<script lang="js">
	export let saveHandler;
  import { character } from '$lib/stores';
	import { onMount } from 'svelte';
  import { generateCharacterPhoto, deleteCharacter, updateCharacter } from '$lib/apis/characters';
  import { goto } from '$app/navigation';

  let localCharacter;
  let isLoading = false;
  
  // let characterPrompt;
  $: localCharacter = $character;

  onMount(() => {
    // console.log(localCharacter)
    // characterPrompt = localCharacter.prompt;
    // console.log(characterPrompt);
  });

  const generatePhoto = async () => {
    isLoading = true;
    await generateCharacterPhoto(localCharacter, localStorage.token);
    isLoading = false;
  }

  const deleteCharacterHandle = async () => {
    await deleteCharacter(localCharacter.id);
    goto('/persona');
  }

  const updateCharacterHandle = async () => {
    const updatedCharacter = localCharacter;
    await updateCharacter(updatedCharacter);
    saveHandler(updatedCharacter);
  }
</script>

<style>
  .character-card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 16px;
    position: relative;
  }
  .avatar-container {
    display: flex;
    gap: 16px;
  }
  .avatar {
    width: 100px;
    height: 100px;
    border-radius: 20%;
    object-fit: cover;
    border: 1px solid #ccc;
  }
  .details {
    flex: 1;
  }
  .attributes {
    text-align: left;
  }
  .attribute {
    margin-bottom: 8px;
  }
  .input-container {
    max-width: 600px;
  }
  .input-container textarea {
    width: 100%;
    height: 100px;
    border-radius: 4px;
    padding: 8px;
    border: 1px solid #ccc;
  }
  .button-container {
    display: flex;
    justify-content: flex-end;
    position: absolute;
    bottom: 16px;
    right: 16px;
  }
  .spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left-color: #000;
    border-radius: 50%;
    width: 16px;
    height: 16px;
    animation: spin 1s linear infinite;
  }
  @keyframes spin {
    to { transform: rotate(360deg); }
  }
</style>

<div class="character-card">
  <div class="avatar-container">
    {#if localCharacter.avatar_url}
      <img class="avatar" src="http://localhost:8080{localCharacter.avatar_url}"  alt="Avatar of {localCharacter.name}" />
    {:else}
      <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="avatar bi bi-person-circle" viewBox="0 0 16 16">
        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
      </svg>
    {/if}
    <div class="details">
      <h1>{localCharacter.name}</h1>
      <div class="attributes">
        <div class="attribute">Age: {localCharacter.age}</div>
        <div class="attribute">Gender: {localCharacter.gender == 0 ? 'Woman' : 'Man'}</div>
        <!-- Additional attributes can be added here -->
      </div>
    </div>
  </div>
  <div class="button-container">
    <button class="generate-photo ml-auto bg-gray-200 text-gray-700 hover:bg-gray-300 font-medium py-2 px-4 rounded" on:click={generatePhoto} disabled={isLoading}>
      {#if isLoading}
        <div class="spinner"></div>
      {:else}
        Generate Photo
      {/if}
    </button>



  </div>
</div>

<div class="input-container">
  <textarea placeholder="Character prompt..." bind:value={localCharacter.prompt}></textarea>
</div>

<button class="update-character bg-blue-500 text-white hover:bg-blue-60 font-medium py-2 px-4 rounded" on:click={updateCharacterHandle}>
  Update Character
</button>

<button class="delete-character bg-red-500 text-white hover:bg-red-600 font-medium py-2 px-4 rounded" on:click={deleteCharacterHandle}>
  Delete Character
</button>