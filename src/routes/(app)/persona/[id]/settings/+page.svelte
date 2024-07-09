<script context="module">
  export async function load({ params }) {
    console.log('Load function called with params:', params);
    const { id } = params;

    try {
      const response = await fetch(`/api/characters/${id}`);
      const character = await response.json();

      if (!response.ok) {
        return {
          status: response.status,
          error: new Error('Could not load character')
        };
      }

      return {
        props: {
          character
        }
      };
    } catch (error) {
      console.error('Error loading character:', error);
      return {
        status: 500,
        error: new Error('Internal Server Error')
      };
    }
  }
</script>

<script>
  import { page } from '$app/stores';
  import CharacterSettings from '$lib/components/persona/CharacterSettings/General.svelte';
</script>

<CharacterSettings characterIdProp={$page.params.id} />
