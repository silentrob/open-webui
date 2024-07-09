<script lang="ts">
  export let saveHandler: Function;
  import { character } from '$lib/stores';
  import { updateCharacter } from '$lib/apis/characters';

  let localCharacter = $character || {};

  let face_shape = localCharacter.appearance?.face_shape;
  let race = localCharacter.appearance?.race;
  let gender = localCharacter.appearance?.gender;

  let body_type = localCharacter.appearance?.body_type;
  let body_build = localCharacter.appearance?.body_build;
  let posture = localCharacter.appearance?.posture;
  let proportions = localCharacter.appearance?.proportions;
  let clothing_style = localCharacter.appearance?.clothing_style;
  
  let skin_texture = localCharacter.appearance?.skin_texture;
  let skin_tone = localCharacter.appearance?.skin_tone;
  let facial_hair = localCharacter.appearance?.facial_hair;

  let hair_color = localCharacter.appearance?.hair_color;
  let hair_length = localCharacter.appearance?.hair_length;
  let hair_style = localCharacter.appearance?.hair_style;
  let hair_texture = localCharacter.appearance?.hair_texture;

  let eyebrows = localCharacter.appearance?.eyebrows;
  let eye_color = localCharacter.appearance?.eye_color;
  let eye_size = localCharacter.appearance?.eye_size;
  let eye_shape = localCharacter.appearance?.eye_shape;

  let age = localCharacter.age;

  const races = ['Caucasian', 'Black', 'Asian', 'Hispanic', 'Mixed'];
  const genders = {0: 'Woman', 1: 'Man', 2: 'Non-binary'};
  
  const faceShapes = ['Oval', 'Round', 'Square', 'Heart', 'Diamond'];
  const skinTone = ['Pale', 'Fair', 'Light', 'Medium', 'Olive', 'Brown', 'Dark'];
  const skinTextures = ['Smooth', 'Wrinkled', 'Freckled', 'Scarred', 'Pockmarked'];
  const facialHair = ['None', 'Clean-shaven', 'Stubble', 'Beard', 'long scruffy beard', 'Mustache', 'Goatee'];

  const hairColors = ['Brown', 'Black', 'Blond', 'White'];
  const hairLengths = ['Bald', 'Short', 'Long', 'Medium'];
  const hairTexture = ['Straight', 'Thick', 'Wavy', 'Curly', 'Coiled', 'Afro'];
  const hairStyles = ['None', 'a Ponytail', 'Braids', 'a Bun', 'Loose', 'a Mohawk', 'Bangs'];

  const eyebrowStyles = ['Thin', 'Thick', 'Arched', 'Straight', 'Bushy'];
  const eyeColors = ['Blue', 'Green', 'Brown', 'Gray'];
  const eyeSizes = ['Small', 'Medium', 'Large'];
  const eyeShapes = ['Almond', 'Oval', 'Round', 'Upturned', 'Downturned'];

  const bodyTypes = ['Short', 'Average', 'Tall'];
  const bodyBuilds = ['Slim', 'Athletic', 'Muscular', 'Stocky', 'Plump', 'Obese'];
  const postures = ['Erect', 'Slouched', 'Graceful', 'Stiff'];
  const proportionsTypes = ['Long-limbed', 'Short-limbed', 'Balanced'];
  const clothingStyles = ['Casual', 'Formal', 'Adventurous', 'Traditional', 'Modern', 'Punk', 'Gothic'];
  

  const updateCharacterHandler = () => {
    localCharacter.age = age;
    localCharacter.gender = gender;
    localCharacter.appearance = {
      face_shape,
      race,

      body_type,
      body_build,
      posture,
      proportions,
      clothing_style,

      skin_texture,
      skin_tone,
      facial_hair,
      hair_color,
      hair_length,
      hair_style,
      hair_texture,
      eyebrows,
      eye_color,
      eye_size,
      eye_shape
    };
    const updatedCharacter = localCharacter;
    updateCharacter(updatedCharacter);
    saveHandler(updatedCharacter);
  };
</script>

<div class="p-6">
  <h1 class="text-2xl font-bold mb-4">Appearance</h1>
  <form on:submit|preventDefault={updateCharacterHandler} class="space-y-6">
    <section class="space-y-4">
      <h2 class="text-xl font-semibold">Character</h2>
      <label class="block">
        Race:
        <select bind:value={race} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each races as r}
            <option value={r}>{r}</option>
          {/each}
        </select>
      </label>

      <label class="block">
        Gender:
        <select bind:value={gender} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each Object.entries(genders) as [key, value]}
            <option value={key}>{value}</option>
          {/each}
        </select>
      </label>

    <label class="block">
      Age: <span>{age}</span>
        <input type="range" min="18" max="90" bind:value={age} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
    </label>
    </section>

    <section class="space-y-4 grid grid-cols-2 gap-4">
      <h2 class="text-xl font-semibold col-span-2">Body Type and Build</h2>
      <label class="block">
        Body Type:
        <select bind:value={body_type} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each bodyTypes as type}
            <option value={type}>{type}</option>
          {/each}
        </select>
      </label>

      <label class="block">
        Build:
        <select bind:value={body_build} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each bodyBuilds as build}
            <option value={build}>{build}</option>
          {/each}
        </select>
      </label>

      <label class="block">
        Posture:
        <select bind:value={posture} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each postures as type}
            <option value={type}>{type}</option>
          {/each}
        </select>
      </label>

      <label class="block">
        Proportions:
        <select bind:value={proportions} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each proportionsTypes as type}
            <option value={type}>{type}</option>
          {/each}
        </select>
      </label>

      <label class="block">
        Clothing Style:
        <select bind:value={clothing_style} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each clothingStyles as style}
            <option value={style}>{style}</option>
          {/each}
        </select>
      </label>

    </section>

    <section class="space-y-4 grid grid-cols-2 gap-4">
      <h2 class="text-xl font-semibold col-span-2">Facial Features</h2>
      <label class="block">
        Face Shape:
        <select bind:value={face_shape} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each faceShapes as shape}
            <option value={shape}>{shape}</option>
          {/each}
        </select>
      </label>

      <label class="block">
        Skin Tone:
        <select bind:value={skin_tone} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each skinTone as tone}
            <option value={tone}>{tone}</option>
          {/each}
        </select>
      </label>

      <label class="block">
        Skin Texture:
        <select bind:value={skin_texture} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each skinTextures as texture}
            <option value={texture}>{texture}</option>
          {/each}
        </select>
      </label>


      <label class="block">
        Facial Hair:
        <select bind:value={facial_hair} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
          {#each facialHair as hair}
            <option value={hair}>{hair}</option>
          {/each}
        </select>
      </label>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-semibold">Hair</h2>
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block">
            Hair Color:
            <select bind:value={hair_color} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
              {#each hairColors as color}
                <option value={color}>{color}</option>
              {/each}
            </select>
          </label>
        </div>
        <div>
          <label class="block">
            Hair Length:
            <select bind:value={hair_length} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
              {#each hairLengths as length}
                <option value={length}>{length}</option>
              {/each}
            </select>
          </label>
        </div>
        <div>
          <label class="block">
            Hair Style:
            <select bind:value={hair_style} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
              {#each hairStyles as style}
                <option value={style}>{style}</option>
              {/each}
            </select>
          </label>
        </div>
        <div>
          <label class="block">
            Hair Texture:
            <select bind:value={hair_texture} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
              {#each hairTexture as texture}
              <option value={texture}>{texture}</option>
            {/each}
            </select>
          </label>
        </div>
      </div>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-semibold">Eyes</h2>
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block">
            Eyebrows:
            <select bind:value={eyebrows} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
              {#each eyebrowStyles as style}
                <option value={style}>{style}</option>
              {/each}
            </select>
          </label>
        </div>
        <div>
          <label class="block">
            Eye Color:
            <select bind:value={eye_color} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
              {#each eyeColors as color}
                <option value={color}>{color}</option>
              {/each}
            </select>
          </label>
        </div>
        <div>
          <label class="block">
            Eye Size:
            <select bind:value={eye_size} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
              {#each eyeSizes as size}
                <option value={size}>{size}</option>
              {/each}
            </select>
          </label>
        </div>
        <div>
          <label class="block">
            Eye Shape:
            <select bind:value={eye_shape} class="mt-1 block w-full p-2 border border-gray-300 rounded-md">
              {#each eyeShapes as shape}
                <option value={shape}>{shape}</option>
              {/each}
            </select>
          </label>
        </div>
      </div>
    </section>

    <button type="submit" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded-md">Save</button>
  </form>
</div>
