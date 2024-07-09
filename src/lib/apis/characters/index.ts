import { WEBUI_API_BASE_URL } from '$lib/constants';
import { imageGenerations } from '$lib/apis/images/index';

export async function getCharacterList() {
  const response = await fetch(`${WEBUI_API_BASE_URL}/characters`);
  return response.json();
}

export async function createCharacter() {
  const response = await fetch(`${WEBUI_API_BASE_URL}/characters/new`, {
    method: 'POST',
  });
  return response.json();
}

export async function getCharacter(id: string) {
  const response = await fetch(`${WEBUI_API_BASE_URL}/characters/${id}`);
  return response.json();
}

export async function updateCharacter(character) {
  
  // Extract only the keys we care about
  const updatedCharacter = {
    id: character.id,
    name: character.name,
    age: character.age,
    gender: character.gender,
    orientation: character.orientation,
    online_status: character.online_status,
    timezone: character.timezone,
    is_role_playing: character.is_role_playing,
    avatar_url: character.avatar_url,
    personality: character.personality,
    prompt: character.prompt,
    appearance: character.appearance,
    long_term_memory: character.long_term_memory,
    short_term_memory: character.short_term_memory,
  };

  // Lets create a custom prompt based on the new updated trait values.
  





  const response = await fetch(`${WEBUI_API_BASE_URL}/characters/${updatedCharacter.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(updatedCharacter),
  });
  return response.json();
}

export async function deleteCharacter(id: string) {
  const response = await fetch(`${WEBUI_API_BASE_URL}/characters/${id}`, {
    method: 'DELETE',
  });
  return response.json();
}

export async function generateCharacterPhoto(character, token: string) {

  console.log(character);
  const age = character.age || '20';
  const gender = (+character.gender === 0) ? 'woman' : 'man';
  const face_shape = character.appearance.face_shape || 'Round'; // Face Shape: Oval, Round, Square, Heart, Diamond
  const race = character.appearance.race || 'mixed';
  
  const bodyType = character.appearance?.body_type || 'Average'; // Body Type: Short, Long, Average
  const bodyBuild = character.appearance?.body_build || 'Slim'; // Body Build: Slim, Average, Full Body
  const posture = character.appearance?.posture || 'Erect'; // Posture: Erect, Graceful, Sitting, Standing
  const proportions = character.appearance?.proportions || 'Balanced'; // Proportions: Balanced, Average, Full Body
  const clothingStyle = character.appearance?.clothing_style || 'Casual'; // Clothing Style: Casual, Formal, Sporty, Casual, Formal, Sporty

  const skin_texture = character.appearance.skin_texture || 'Smooth'; // Skin Texture: Smooth, Wrinkled, Freckled, Scarred, Pockmarked
  const skin_tone = character.appearance.skin_tone || 'Fair'; // Skin Tone: Fair, Light, Medium, Olive, Brown, Dark
  const facial_hair = character.appearance.facial_hair || 'None'; // Facial Hair: None, Beard, Moustache, Goatee, Sideburns, Mustache

  const hair_color = character.appearance.hair_color || 'Brown'; // Hair Color: Brown, Black, Blond, White
  const hair_length = character.appearance.hair_length || 'long'; // Hair Length: Bald, Short, Long, Medium
  const hair_texture = character.appearance.hair_texture || 'Straight'; // Hair Texture: Straight, Thick, Wavy, Curly, Coiled, Afro
  const hair_style = character.appearance.hair_style || 'None'; // Hair Style: None, Ponytail, Braids, Bun, Loose, Mohawk

  const eyebrows = character.appearance.eyebrows || 'Thick'; // Eyebrows: Thin, Thick, Arched, Straight, Bushy
  const eye_color = character.appearance.eye_color || 'Brown'; // Eye Color: Blue, Green, Brown, Gray
  const eye_size = character.appearance.eye_size || 'Large'; // Eye Size: Small, Medium, Large
  const eye_shape = character.appearance.eye_shape || 'Almond'; // Eye Shape: Almond, Oval, Round, Upturned, Downturned
  
  // Closeup half body portrait
  // Full body portrait
  const general = `Closeup half body candid photo, ${+character.gender == 0 && posture == 'Graceful' ? 'beautiful' : '' } ${gender}, ${age} years old, ${race},`;
  const body = `${bodyType} figure, ${bodyBuild} body, ${posture} posture, ${proportions} proportions,`;
  let face = ` ${face_shape} face, slight smile, ${skin_tone} skin tone, ${skin_texture} skin, (no makeup)`;
  if (facial_hair !== 'None') {
    face = `${face} with ${facial_hair},`;
  }

  const eyes = `${eyebrows} eyebrows, ${eye_size} ${eye_shape} ${eye_color} eyes,`;
  // beautiful intricate 
  let hair = `${hair_length} ${hair_texture} ${hair_color} hair,`;
  if (hair_length === 'Bald') {
    hair = `${hair_length} ${hair_color} hair,`;
  }
  if (hair_style !== 'None') {
    hair = `${hair} with ${hair_style},`;
  }
  const style = `(${clothingStyle} clothing:1.3),`;
  const camera = `symmetrical, soft lighting, detailed face`;//, sitting in a chair, looking into camera`;
  const prompt = `${general} ${body} ${face} ${eyes} ${hair} ${style} ${camera}`;
  
  console.log(prompt);

  const image = await imageGenerations(token, prompt);
  if (image) {
    character.avatar_url = image[0].url;
    updateCharacter(character);
  }

  return true;
}
