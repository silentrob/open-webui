from pydantic import BaseModel
from typing import List, Dict

class PersonalityTraits(BaseModel):
    emotional: Dict[str, int]
    social: Dict[str, int]
    cognitive: Dict[str, int]
    behavioral: Dict[str, int]
    physical_health: Dict[str, int]
    moral: Dict[str, int]
    communication: Dict[str, int]

class Personality(BaseModel):
    traits: PersonalityTraits
    relationship: Dict[str, int]

class Appearance(BaseModel):
    face_shape: str
    race: str
    body_type: str
    body_build: str
    posture: str
    proportions: str
    clothing_style: str
    skin_texture: str
    skin_tone: str
    facial_hair: str
    hair_color: str
    hair_length: str
    hair_style: str
    hair_texture: str
    eyebrows: str
    eye_color: str
    eye_size: str
    eye_shape: str

class Character(BaseModel):
    id: str
    name: str
    age: int
    gender: int
    orientation: int
    online_status: int
    timezone: str
    is_role_playing: bool
    avatar_url: str
    prompt: str
    personality: Personality
    long_term_memory: List[str]
    short_term_memory: List[str]
    appearance: Appearance
