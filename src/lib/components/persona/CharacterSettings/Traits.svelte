<script lang="js">
  import { getContext } from 'svelte';
  import { character } from '$lib/stores';
  import { updateCharacter } from '$lib/apis/characters';
  export let saveHandler;

  let localCharacter;
  $: localCharacter = $character;

  const updateTraits = async () => {
    const updatedCharacter = localCharacter;
    await updateCharacter(updatedCharacter);
    saveHandler(updatedCharacter);
  }
</script>

<!-- List out the Character's traits -->
<div class="px-5 pt-4 pb-2 w-full ">
  {#each Object.entries(localCharacter?.personality?.traits || {}) as [name, trait]}
    <div class="trait-group mt-8">
      <h3 class="text-lg font-bold">{name.replace(/([A-Z])/g, ' $1').replace(/^./, (match) => match.toUpperCase())}</h3>
      <div class="traits-grid">
        {#each Object.entries(trait) as [subName, traitValue]}
          <div class="trait-item">
            <div class="text-sm text-gray-500">{(subName.charAt(0).toUpperCase() + subName.slice(1).toLowerCase())}: <span class="text-black" data-trait-value={traitValue}>{traitValue}</span></div>
            <input type="range" min="1" max="10" bind:value={localCharacter.personality.traits[name][subName]} class="slider w-64">
          </div>
        {/each}
      </div>
    </div>
  {/each}

  <!-- Add a button to update the traits -->
  <button on:click={updateTraits} class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4">Update Traits</button>
</div>

<style>
  .traits-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  .trait-item {
    display: flex;
    flex-direction: column;
  }
</style>
