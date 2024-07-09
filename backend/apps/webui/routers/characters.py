from fastapi import APIRouter, HTTPException
import json
import logging
from apps.persona.character import CharacterAgent
from apps.webui.models.character import Character
from apps.persona.tropes import get_random_trope
from faker import Faker

router = APIRouter()
log = logging.getLogger(__name__)

@router.put('/{id}')
def update_character(id: str, character: Character):
    log.info(f"UPDATING CHARACTER {id}")
    try:
        CharacterAgent.update_character(id, character)
    except Exception as e:
        log.error(f"Error updating character: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return character

@router.delete('/{id}')
def delete_character(id: str):
  log.info(f"DELETING CHARACTER {id}")
  CharacterAgent.delete_character(id)
  return {"message": "Character deleted"}

@router.get('/')
def get_characters():
  log.info("GETTING CHARACTERS")

  all_characters = CharacterAgent.get_all_characters()
  return all_characters

@router.get('/{id}')
def get_character(id: str):
  log.info(f"GETTING CHARACTER {id}")
  character = CharacterAgent.get_character(id)
  return character

@router.post('/new')
def new_character():
  fake = Faker()
  gender = fake.random_element(elements=('male', 'female'))
  first_name = fake.first_name_male() if gender == 'male' else fake.first_name_female()
  character = CharacterAgent.create_character(first_name, (gender == 'male' and 1 or 0), get_random_trope())
  return character
