<script>
  import { goto } from '$app/navigation';
  import { tick, onMount } from 'svelte';
  import { character } from '$lib/stores';
	import { toast } from 'svelte-sonner';

  import GeneralInfo from './GeneralInfo.svelte';
  import Appearance from './Appearance.svelte';
  import Traits from './Traits.svelte';

  import { getCharacter } from '$lib/apis/characters';

  export let characterIdProp;
  let loaded = false;

  $: if (characterIdProp) {
    loadCharacter().then(characterData => {
      if (characterData) {
        tick().then(() => loaded = true);
      } else {
        goto('/');
      }
    });
  }

  async function loadCharacter() {
    const characterData = await getCharacter(characterIdProp);
    character.set(characterData);
    return characterData;
  }
  onMount(async () => {
    if (!characterIdProp) {
      await goto('/');
    }
  });

  let selectedTab = 'general';

</script>
<div class="mx-4 w-full">
  <div class="flex flex-col lg:flex-row  h-full py-2 lg:space-x-4">
    <div
      class="tabs flex flex-row overflow-x-auto space-x-1 max-w-full lg:space-x-0 lg:space-y-1 lg:flex-col lg:flex-none lg:w-44 dark:text-gray-200 text-xs text-left scrollbar-none"
    >
      <button
        class="px-2.5 py-2.5 min-w-fit rounded-lg flex-1 lg:flex-none flex text-right transition {selectedTab ===
        'general'
          ? 'bg-gray-200 dark:bg-gray-800'
          : ' hover:bg-gray-300 dark:hover:bg-gray-850'}"
        on:click={() => {
          selectedTab = 'general';
        }}
      >
        <div class=" self-center mr-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 16 16"
            fill="currentColor"
            class="w-4 h-4"
          >
            <path
              fill-rule="evenodd"
              d="M6.955 1.45A.5.5 0 0 1 7.452 1h1.096a.5.5 0 0 1 .497.45l.17 1.699c.484.12.94.312 1.356.562l1.321-1.081a.5.5 0 0 1 .67.033l.774.775a.5.5 0 0 1 .034.67l-1.08 1.32c.25.417.44.873.561 1.357l1.699.17a.5.5 0 0 1 .45.497v1.096a.5.5 0 0 1-.45.497l-1.699.17c-.12.484-.312.94-.562 1.356l1.082 1.322a.5.5 0 0 1-.034.67l-.774.774a.5.5 0 0 1-.67.033l-1.322-1.08c-.416.25-.872.44-1.356.561l-.17 1.699a.5.5 0 0 1-.497.45H7.452a.5.5 0 0 1-.497-.45l-.17-1.699a4.973 4.973 0 0 1-1.356-.562L4.108 13.37a.5.5 0 0 1-.67-.033l-.774-.775a.5.5 0 0 1-.034-.67l1.08-1.32a4.971 4.971 0 0 1-.561-1.357l-1.699-.17A.5.5 0 0 1 1 8.548V7.452a.5.5 0 0 1 .45-.497l1.699-.17c.12-.484.312-.94.562-1.356L2.629 4.107a.5.5 0 0 1 .034-.67l.774-.774a.5.5 0 0 1 .67-.033L5.43 3.71a4.97 4.97 0 0 1 1.356-.561l.17-1.699ZM6 8c0 .538.212 1.026.558 1.385l.057.057a2 2 0 0 0 2.828-2.828l-.058-.056A2 2 0 0 0 6 8Z"
              clip-rule="evenodd"
            />
          </svg>
        </div>
        <div class=" self-center">General</div>
      </button>

      <button
      class="px-2.5 py-2.5 min-w-fit rounded-lg flex-1 lg:flex-none flex text-right transition {selectedTab ===
      'appearance'
        ? 'bg-gray-200 dark:bg-gray-800'
        : ' hover:bg-gray-300 dark:hover:bg-gray-850'}"
      on:click={() => {
        selectedTab = 'appearance';
      }}
    >
      <div class=" self-center mr-2">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 16 16"
          fill="currentColor"
          class="w-4 h-4"
        >
          <path
            fill-rule="evenodd"
            d="M6.955 1.45A.5.5 0 0 1 7.452 1h1.096a.5.5 0 0 1 .497.45l.17 1.699c.484.12.94.312 1.356.562l1.321-1.081a.5.5 0 0 1 .67.033l.774.775a.5.5 0 0 1 .034.67l-1.08 1.32c.25.417.44.873.561 1.357l1.699.17a.5.5 0 0 1 .45.497v1.096a.5.5 0 0 1-.45.497l-1.699.17c-.12.484-.312.94-.562 1.356l1.082 1.322a.5.5 0 0 1-.034.67l-.774.774a.5.5 0 0 1-.67.033l-1.322-1.08c-.416.25-.872.44-1.356.561l-.17 1.699a.5.5 0 0 1-.497.45H7.452a.5.5 0 0 1-.497-.45l-.17-1.699a4.973 4.973 0 0 1-1.356-.562L4.108 13.37a.5.5 0 0 1-.67-.033l-.774-.775a.5.5 0 0 1-.034-.67l1.08-1.32a4.971 4.971 0 0 1-.561-1.357l-1.699-.17A.5.5 0 0 1 1 8.548V7.452a.5.5 0 0 1 .45-.497l1.699-.17c.12-.484.312-.94.562-1.356L2.629 4.107a.5.5 0 0 1 .034-.67l.774-.774a.5.5 0 0 1 .67-.033L5.43 3.71a4.97 4.97 0 0 1 1.356-.561l.17-1.699ZM6 8c0 .538.212 1.026.558 1.385l.057.057a2 2 0 0 0 2.828-2.828l-.058-.056A2 2 0 0 0 6 8Z"
            clip-rule="evenodd"
          />
        </svg>
      </div>
      <div class=" self-center">Appearance</div>
    </button>
    
    <button
      class="px-2.5 py-2.5 min-w-fit rounded-lg flex-1 lg:flex-none flex text-right transition {selectedTab ===
      'traits'
        ? 'bg-gray-200 dark:bg-gray-800'
        : ' hover:bg-gray-300 dark:hover:bg-gray-850'}"
      on:click={() => {
        selectedTab = 'traits';
      }}
    >
      <div class=" self-center mr-2">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 16 16"
          fill="currentColor"
          class="w-4 h-4"
        >
          <path
            fill-rule="evenodd"
            d="M6.955 1.45A.5.5 0 0 1 7.452 1h1.096a.5.5 0 0 1 .497.45l.17 1.699c.484.12.94.312 1.356.562l1.321-1.081a.5.5 0 0 1 .67.033l.774.775a.5.5 0 0 1 .034.67l-1.08 1.32c.25.417.44.873.561 1.357l1.699.17a.5.5 0 0 1 .45.497v1.096a.5.5 0 0 1-.45.497l-1.699.17c-.12.484-.312.94-.562 1.356l1.082 1.322a.5.5 0 0 1-.034.67l-.774.774a.5.5 0 0 1-.67.033l-1.322-1.08c-.416.25-.872.44-1.356.561l-.17 1.699a.5.5 0 0 1-.497.45H7.452a.5.5 0 0 1-.497-.45l-.17-1.699a4.973 4.973 0 0 1-1.356-.562L4.108 13.37a.5.5 0 0 1-.67-.033l-.774-.775a.5.5 0 0 1-.034-.67l1.08-1.32a4.971 4.971 0 0 1-.561-1.357l-1.699-.17A.5.5 0 0 1 1 8.548V7.452a.5.5 0 0 1 .45-.497l1.699-.17c.12-.484.312-.94.562-1.356L2.629 4.107a.5.5 0 0 1 .034-.67l.774-.774a.5.5 0 0 1 .67-.033L5.43 3.71a4.97 4.97 0 0 1 1.356-.561l.17-1.699ZM6 8c0 .538.212 1.026.558 1.385l.057.057a2 2 0 0 0 2.828-2.828l-.058-.056A2 2 0 0 0 6 8Z"
            clip-rule="evenodd"
          />
        </svg>
      </div>
      <div class=" self-center">Traits</div>
    </button>  
    </div>



    <div class="flex-1 mt-3 lg:mt-0 overflow-y-scroll">
      {#if selectedTab === 'general'}
        <GeneralInfo
          saveHandler={() => {
            toast.success('Settings saved successfully!');
          }}
        />
      {:else if selectedTab === 'appearance'}
        <Appearance
          saveHandler={() => {
            toast.success('Settings saved successfully!');
          }}
        />
      {:else if selectedTab === 'traits'}
        <Traits
          saveHandler={() => {
            toast.success('Settings saved successfully!');
          }}
        />
      {/if}
    
    </div>


  </div>
</div>