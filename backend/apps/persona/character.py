from apps.persona.personality import Personality
from enum import Enum
import logging
import json
import sqlite3
import shortuuid

log = logging.getLogger(__name__)

class GENDER(Enum):
  UNKNOWN = -1
  FEMALE = 0
  MALE = 1
  OTHER = 2

class ORIENTATION(Enum):
  UNKNOWN = -1
  STRAIGHT = 0
  GAY = 1
  BISEXUAL = 2
  ASEXUAL = 3
  PANSEXUAL = 4
  OTHER = 5

class ONLINESTATUS(Enum):
  OFFLINE = 0
  ONLINE = 1
  AWAY = 2
  BUSY = 3

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.name  # Serialize enum objects by their name
        return super().default(obj)

def initialize_db():
    conn = sqlite3.connect('./apps/persona/character_agents.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS character_agents (
            id TEXT PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender INTEGER,
            orientation INTEGER,
            online_status INTEGER,
            timezone TEXT,
            is_role_playing BOOLEAN,
            personality TEXT,
            prompt TEXT,
            avatar_url TEXT,
            appearance TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS relationships (
            character_id TEXT,
            user_id TEXT,
            traits TEXT,
            PRIMARY KEY (character_id, user_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized")

class CharacterAgent:
    def __init__(self, id, name, gender=GENDER.UNKNOWN, trope=None, appearance=None):
        self.id = id
        self.name = name
        self.age = 26
        self.gender = gender
        self.orientation = ORIENTATION.UNKNOWN
        self.online_status = ONLINESTATUS.OFFLINE
        self.timezone = 'UTC'
        self.is_role_playing = False
        self.prompt = ''
        self.avatar_url = ''
        self.appearance = appearance if appearance else {
            'face_shape': '',
            'race': '',
            'body_type': '',
            'body_build': '',
            'posture': '',
            'proportions': '',
            'clothing_style': '',
            'skin_texture': '',
            'skin_tone': '',
            'facial_hair': '',
            'hair_color': '',
            'hair_length': '',
            'hair_style': '',
            'hair_texture': '',
            'eyebrows': '',
            'eye_color': '',
            'eye_size': '',
            'eye_shape': ''
        }
        
        if trope:
            self.personality = Personality(trope)
        else:
            self.personality = Personality()  # Initialize with default parameters
        
        self.long_term_memory = []
        self.short_term_memory = []
        self.relationships = {}

    def get_relationship_traits(self, user_id):
        if user_id not in self.relationships:
            relationship_traits = self.personality.relationship
            self.relationships[user_id] = relationship_traits
            self.save_relationships_to_db()
        
        return self.relationships[user_id]
    
    def save_to_db(self):
        conn = sqlite3.connect('./apps/persona/character_agents.db')
        cursor = conn.cursor()
        
        # Convert GENDER, ORIENTATION, and ONLINESTATUS enums to their values before serialization
        gender_value = self.gender.value
        orientation_value = self.orientation.value
        online_status_value = self.online_status.value
        
        # Ensure personality is a dictionary before serialization
        personality_dict = self.personality.to_dict() if isinstance(self.personality, Personality) else self.personality
        
        cursor.execute('''
            INSERT OR REPLACE INTO character_agents (id, name, age, gender, orientation, online_status, timezone, is_role_playing, personality, prompt, avatar_url, appearance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.id, self.name, self.age, gender_value, orientation_value, online_status_value, self.timezone, self.is_role_playing, json.dumps(personality_dict, cls=CustomEncoder), self.prompt, self.avatar_url, json.dumps(self.appearance)))
        
        conn.commit()
        conn.close()

    @classmethod
    def load_from_db(cls, id):
        conn = sqlite3.connect('./apps/persona/character_agents.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, age, gender, orientation, online_status, timezone, is_role_playing, personality, prompt, avatar_url, appearance FROM character_agents WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            id, name, age, gender, orientation, online_status, timezone, is_role_playing, personality_data, prompt, avatar_url, appearance_data = row
            agent = cls(id, name)
            agent.age = age
            agent.gender = GENDER(gender)
            agent.orientation = ORIENTATION(orientation)
            agent.online_status = ONLINESTATUS(online_status)
            agent.timezone = timezone
            agent.is_role_playing = is_role_playing == 1
            agent.personality.__dict__ = json.loads(personality_data)
            agent.prompt = prompt
            agent.avatar_url = avatar_url
            agent.appearance = json.loads(appearance_data)
            
            # Load relationships from the relationships table
            agent.relationships = cls.load_relationships_from_db(id)
            
            return agent
        return None

    @classmethod
    def get_all_characters(cls):
        conn = sqlite3.connect('./apps/persona/character_agents.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, age, gender, orientation, online_status, timezone, is_role_playing, personality, prompt, avatar_url, appearance FROM character_agents')
        rows = cursor.fetchall()
        conn.close()
        
        characters = []
        for row in rows:
            id, name, age, gender, orientation, online_status, timezone, is_role_playing, personality_data, prompt, avatar_url, appearance_data = row
            agent = cls(id, name)
            agent.age = age
            agent.gender = GENDER(gender)
            agent.orientation = ORIENTATION(orientation)
            agent.online_status = ONLINESTATUS(online_status)
            agent.timezone = timezone
            agent.is_role_playing = is_role_playing == 1
            agent.personality.__dict__ = json.loads(personality_data)
            agent.prompt = prompt
            agent.avatar_url = avatar_url
            agent.appearance = json.loads(appearance_data)
            characters.append(agent)
        
        return characters

    @classmethod
    def create_character(cls, name, gender, trope=None):
        id = shortuuid.uuid()
        new_character = cls(id, name, GENDER(gender), trope)
        new_character.save_to_db()
        return new_character

    @staticmethod
    def get_character(id):
        conn = sqlite3.connect('./apps/persona/character_agents.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, age, gender, orientation, online_status, timezone, is_role_playing, personality, prompt, avatar_url, appearance FROM character_agents WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            id, name, age, gender, orientation, online_status, timezone, is_role_playing, personality_data, prompt, avatar_url, appearance_data = row
            agent = CharacterAgent(id, name)
            agent.age = age
            agent.gender = GENDER(gender)
            agent.orientation = ORIENTATION(orientation)
            agent.online_status = ONLINESTATUS(online_status)
            agent.timezone = timezone
            agent.is_role_playing = is_role_playing == 1
            agent.personality.__dict__ = json.loads(personality_data)
            agent.prompt = prompt
            agent.avatar_url = avatar_url
            agent.appearance = json.loads(appearance_data)
            return agent
        return None

    @staticmethod
    def update_character(id: str, character):
        log.info(f"Character ID: {id}")
        log.info(f"Character Data: {character}")

        try:
            # Assuming character is a Pydantic model, convert to dict if needed
            character_data = character.dict() if hasattr(character, 'dict') else character

            # Log the character data to debug
            log.info(f"Character Data (dict): {character_data}")

            # Convert integer values to their respective enum types
            character_data['gender'] = GENDER(character_data['gender'])
            character_data['orientation'] = ORIENTATION(character_data['orientation'])
            character_data['online_status'] = ONLINESTATUS(character_data['online_status'])

            # Ensure personality is a dictionary
            if isinstance(character_data['personality'], Personality):
                character_data['personality'] = character_data['personality'].to_dict()

            # Log the converted data
            log.info(f"Converted Character Data: {character_data}")

            # Actual update logic here
            agent = CharacterAgent.get_character(id)
            if agent:
                agent.__dict__.update(character_data)
                agent.save_to_db()
            else:
                raise ValueError(f"Character with ID {id} not found")

        except Exception as e:
            log.error(f"Error in update_character: {e}")
            raise

        return character

    @staticmethod
    def delete_character(id):
        conn = sqlite3.connect('./apps/persona/character_agents.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM character_agents WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    def __str__(self):
        return (f"CharacterAgent(id={self.id}, name={self.name}, "
                f"gender={self.gender}, orientation={self.orientation}, online_status={self.online_status}, timezone={self.timezone}, "
                f"is_role_playing={self.is_role_playing}, "
                f"personality={self.personality}, "
                f"relationships={self.relationships}, "
                f"appearance={self.appearance})")
  
    def save_relationships_to_db(self):
        conn = sqlite3.connect('./apps/persona/character_agents.db')
        cursor = conn.cursor()
        
        for user_id, traits in self.relationships.items():
            cursor.execute('INSERT OR REPLACE INTO relationships (character_id, user_id, traits) VALUES (?, ?, ?)', (self.id, user_id, json.dumps(traits)))
        
        conn.commit()
        conn.close()

    @classmethod
    def load_relationships_from_db(cls, character_id):
        conn = sqlite3.connect('./apps/persona/character_agents.db')
        cursor = conn.cursor()
        cursor.execute('SELECT user_id, traits FROM relationships WHERE character_id = ?', (character_id,))
        rows = cursor.fetchall()
        conn.close()
        
        relationships = {}
        for row in rows:
            user_id, traits_data = row
            relationships[user_id] = json.loads(traits_data)
        
        return relationships

def add_friend(self, user_id):
        if user_id not in self.relationships:
            relationship_traits = self.personality.relationship
            self.relationships[user_id] = relationship_traits
  
if __name__ == '__main__':
  print("Main")