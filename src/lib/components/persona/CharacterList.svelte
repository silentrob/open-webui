<script lang="js">
  import { onMount } from 'svelte';

  let characters = [];
  import { getCharacterList } from '$lib/apis/characters/index';
  import { goto } from '$app/navigation';
  onMount(async () => {
    characters = await getCharacterList();
    console.log(characters)
  });
</script>

<style>
  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    object-fit: cover;
  }
</style>

<div class="px-1.5 flex flex-col space-y-2">
  {#each characters as character}
    <div class="flex space-x-3 rounded-xl px-2.5 py-2 hover:bg-gray-100 dark:hover:bg-gray-900 transition items-center"
      on:click={() => goto(`/persona/${character.id}/settings`)}
    >
      <span class="relative inline-flex size-2">
        {#if !character.online}
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"/>
          <span class="relative inline-flex rounded-full size-2 bg-green-500" />
        {:else}
          <span class="relative inline-flex rounded-full size-2 bg-red-500" />
        {/if}
      </span>
      <img class="avatar" src={character.avatar_url !== "" ? `http://localhost:8080${character.avatar_url}` : '/user.png'} alt="Avatar of {character.name}" />
      <div class="flex flex-col">
        <div class="font-medium text-sm">{character.name}</div>
      </div>
    </div>
  {/each}
</div>