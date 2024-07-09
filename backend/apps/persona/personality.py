import math
from apps.persona.tropes import get_personality_tropes

# Helper Class for managing personaity traits
# TODO: Sort out the polarity, up should mean the same thing in all cases.
emotional_traits = [
  "RECONCILIATION",       # Vindictiveness ↔ Forgiveness
  "BENEVOLENCE",          # Kindness ↔ Cruelty
  "SELF-CONFIDENCE",      # Assurance ↔ Insecurity
  "CONSISTENCY",          # Capriciousness ↔ Stability
  "MODESTY",              # Hubris ↔ Humility
  "RESILIENCE",           # Fragility ↔ Strength
  "APPRECIATION",         # Entitlement ↔ Gratitude
  "GENTLENESS",           # Tenderness ↔ Harshness
  "EMOTIONAL_EXPRESSION", # Expressivity ↔ Inhibition
  "SELF-ESTEEM",          # Confidence ↔ Self-Doubt
  "COURAGE",              # Timidity ↔ Bravery
  "EMPATHY",              # Sociopathy ↔ Empathy
  "SEXUALITY",            # Sensuality ↔ Asexuality
  "HAPPINESS",            # Joy ↔ Sadness
  "ANGER",                # Anger ↔ Serenity
  "TRANQUILITY",          # Calmness ↔ Anxiety
  "OUTLOOK",              # Optimism ↔ Pessimism
  "SELF-CONTROL",         # Patience ↔ Impulsiveness
  "TRUSTWORTHINESS",      # Trust ↔ Suspicion
  "GENEROSITY",           # Altruism ↔ Selfishness
  "COMPASSION"            # Compassion ↔ Indifference
]

social_traits = [
  "KINDNESS",             # Kindness ↔ Cruelty
  "FRIENDLINESS",         # Friendliness ↔ Hostility
  "CONFIDENCE",           # Confidence ↔ Insecurity
  "CHARISMA",             # Charisma ↔ Awkwardness
  "EMPATHY",              # Indifference ↔ Empathy  
  "LOYALTY",              # Loyalty ↔ Betrayal
  "COMPASSION",           # Compassion ↔ Indifference
  "ALTRUISM"              # Altruism ↔ Selfishness
]

cognitive_traits = [
  "KNOWLEDGE"             # Knowledge ↔ Ignorance
  "INNOVATION",           # Innovation ↔ Conventionality
  "APTITUDE",             # Facility ↔ Ineptitude
  "WISDOM",               # Wisdom ↔ Foolishness
  "EDUCATION",            # Education ↔ Ignorance
  "DECISIVENESS",         # Decisiveness ↔ Indecisiveness
  "INTUITION",            # Intuition ↔ Rationality
  "CURIOSITY",            # Curiosity ↔ Apathy
  "MEMORY",               # Memory ↔ Forgetfulness
]

behavioral_traits = [
  "COORDINATION",         # Coordination ↔ Uncoordination
  "INDUSTRY",             # Laziness ↔ Industry
  "WHIMSY",               # Whimsy ↔ Seriousness
  "EXTROVERSION",         # Introversion ↔ Extroversion
  "COMPETITIVENESS",      # Competitiveness ↔ Cooperativeness
  "WANDERLUST",           # Wanderlust ↔ Contentment
  "TENACITY"              # Tenacity ↔ Resignation
]

physical_health_traits = [
  "POSE_AND_GRACE",       # Rhythm ↔ Arrhythmia
  "FASHIONABLENESS",      # Fashionableness ↔ Unfashionableness
  "STRENGTH"              # Strength ↔ Weakness
]

moral_traits = [
  "INTEGRITY",            # Integrity ↔ Corruption
  "MORALITY",             # Morality ↔ Immorality
  "FIDELITY",             # Fidelity ↔ Infidelity
  "SPIRITUALITY",         # Spirituality ↔ Materialism
  "FAITH",                # Faith ↔ Skepticism
  "PATRIOTISM",           # Patriotism ↔ Apathy
  "HUMILITY",             # Humility ↔ Arrogance
  "HUMOR",                # Humor ↔ Seriousness
  "SINCERITY"             # Sarcasm ↔ Sincerity
]

communication_traits = [
  "EXTROVERSION",         # This is linked to `behavioral_traits`. Influences how energetic and engaging someone is in conversation.
  "AGREEABLENESS",        # Affects the warmth and politeness of interactions. 
  "OPENNESS",             # This is linked to `social_traits`. Contributes to the creativity and depth of expression.
  "CONSCIENTIOUSNESS",    # Ensures clarity and thoroughness in communication.
  "NEUROTICISM",          # Can lead to variability in tone and expressiveness based on emotional stability.
  "ASSERTIVENESS",        # Determines the level of confidence and clarity in delivering messages.
]

class Personality:
    def __init__(self, trope_name=None, traits=None, relationship=None):
        if traits and relationship:
            self.traits = traits
            self.relationship = relationship
        else:
            if trope_name:
                self.traits = self.init_personality_traits(trope_name)
            else:
                self.traits = self.init_default_traits()
            self.relationship = self.init_relationship_traits()

    def to_dict(self):
        return {
            "traits": self.traits,
            "relationship": self.relationship
        }

    @classmethod
    def from_dict(cls, data):
        return cls(traits=data.get('traits'), relationship=data.get('relationship'))

    def init_default_traits(self):
        # Define default traits here
        default_traits = {
            'emotional': {trait: 5 for trait in emotional_traits},
            'social': {trait: 5 for trait in social_traits},
            'cognitive': {trait: 5 for trait in cognitive_traits},
            'behavioral': {trait: 5 for trait in behavioral_traits},
            'physical_health': {trait: 5 for trait in physical_health_traits},
            'moral': {trait: 5 for trait in moral_traits},
            'communication': {trait: 5 for trait in communication_traits}
        }
        return default_traits

    def init_relationship_traits(self):
        influences = {
            'TRUST': ['RECONCILIATION', 'EMPATHY', 'TRUSTWORTHINESS', 'LOYALTY'],
            'RESPECT': ['RECONCILIATION', 'MODESTY', 'KNOWLEDGE', 'INNOVATION', 'APTITUDE', 'WISDOM', 'EDUCATION'],
            'AFFECTION': ['BENEVOLENCE', 'APPRECIATION', 'GENTLENESS', 'KINDNESS', 'FRIENDLINESS', 'COMPASSION', 'ALTRUISM'],
            'COMMUNICATION': ['EMOTIONAL_EXPRESSION', 'SELF-ESTEEM', 'CONFIDENCE', 'CHARISMA', 'CURIOSITY'],
            'SUPPORT': ['BENEVOLENCE', 'RESILIENCE', 'APPRECIATION', 'HAPPINESS', 'TRANQUILITY', 'GENEROSITY', 'COMPASSION', 'KINDNESS', 'ALTRUISM'],
            'CONFLICT': ['RESILIENCE', 'GENTLENESS', 'ANGER', 'TRANQUILITY', 'SELF-CONTROL'],
            'INTIMACY': ['MODESTY', 'COURAGE', 'EMPATHY', 'SEXUALITY'],
            'DEPENDENCY': [],  # No influences, usually low initially
            'COMPATIBILITY': ['CONSISTENCY', 'OUTLOOK', 'CHARISMA', 'INTUITION', 'KNOWLEDGE', 'INNOVATION', 'APTITUDE', 'WISDOM', 'EDUCATION'],
            'COMMITMENT': ['SELF-CONFIDENCE', 'COURAGE', 'SELF-ESTEEM', 'DECISIVENESS', 'LOYALTY', 'SELF-CONTROL']
        }

        base_values = {
            'TRUST': 5,
            'RESPECT': 5,
            'AFFECTION': 3,
            'COMMUNICATION': 5,
            'SUPPORT': 3,
            'CONFLICT': 5,
            'INTIMACY': 2,
            'DEPENDENCY': 2,
            'COMPATIBILITY': 5,
            'COMMITMENT': 3
        }

        relationship = base_values.copy()

        for trait, influence_list in influences.items():
            if influence_list:  # Check if the influence list is not empty
                influence_sum = sum((self.get_trait_value(influence) - 5) * 1.5 for influence in influence_list)
                if trait == 'CONFLICT':
                    relationship[trait] -= math.ceil(influence_sum // len(influence_list))
                else:
                    relationship[trait] += math.ceil(influence_sum // len(influence_list))
        
        return relationship

    def get_trait_value(self, trait_name):
        for category in self.traits.values():
            if trait_name in category:
                return category[trait_name]
        return 5  # Default value if trait not found

    # Gets the trait at the specified offset
    def __getitem__(self, type):
        return self.traits[type]

    def __setitem__(self, type, value):
        self.traits[type] = value
        self.init_relationship_traits()

    # Helper that really has no business being a class method
    def clamp(self, value, min_value=0, max_value=10):
        return max(min_value, min(value, max_value))

    def init_personality_traits(self, trope_name):

        tropes = get_personality_tropes()
        if trope_name not in tropes:
            valid_tropes = ', '.join(tropes.keys())
            raise ValueError(f"Trope '{trope_name}' not found in personality tropes. Valid tropes are: {valid_tropes}.")
        traits = tropes[trope_name]

        # Calculate communication traits based on influences
        traits['communication'] = {}
        traits['communication']['EXTROVERSION'] = self.clamp(int(5 + 0.5 * ((traits['behavioral']['EXTROVERSION'] - 5) + (traits['behavioral']['WHIMSY'] - 5))))
        traits['communication']['AGREEABLENESS'] = self.clamp(int(5 + 0.5 * ((traits['social']['KINDNESS'] - 5) + (traits['social']['FRIENDLINESS'] - 5) + (traits['social']['COMPASSION'] - 5))))
        traits['communication']['OPENNESS'] = self.clamp(int(5 + 0.5 * ((traits['social']['KINDNESS'] - 5) + (traits['cognitive']['CURIOSITY'] - 5))))
        traits['communication']['CONSCIENTIOUSNESS'] = self.clamp(int(5 + 0.5 * ((traits['cognitive']['APTITUDE'] - 5) + (traits['cognitive']['DECISIVENESS'] - 5))))
        traits['communication']['NEUROTICISM'] = self.clamp(int(5 - 0.5 * ((traits['emotional']['RESILIENCE'] - 5) + (traits['emotional']['SELF-CONTROL'] - 5))))
        traits['communication']['ASSERTIVENESS'] = self.clamp(int(5 + 0.5 * ((traits['emotional']['SELF-CONFIDENCE'] - 5) + (traits['social']['CONFIDENCE'] - 5))))
        return traits;

    # Prints only the traits that have changed
    def __str__(self):
        traits_str = []
        for category, traits in self.traits.items():
            category_str = []
            for trait, value in traits.items():
                if value != 5:
                    category_str.append(f"  {trait}: {value}")
            if category_str:
                traits_str.append(f"{category.capitalize()} Traits:")
                traits_str.extend(category_str)
        return "\n".join(traits_str)


    # Prints all the trail k:v
    def debug(self):
        traits_str = []
        for category, traits in self.traits.items():
            traits_str.append(f"{category.capitalize()} Traits:")
            for trait, value in traits.items():
                traits_str.append(f"  {trait}: {value}")
        return "\n".join(traits_str)
