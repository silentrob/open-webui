relationship_traits = [
  'TRUST',
  'RESPECT',
  'AFFECTION',
  'COMMUNICATION',
  'SUPPORT',
  'CONFLICT',
  'INTIMACY',
  'DEPENDENCY',
  'COMPATIBILITY',
  'COMMITMENT'
]

emotional_traits = [
  "RECONCILIATION",       # Vindictiveness ↔ Forgiveness
  "BENEVOLENCE",          # Kindness ↔ Cruelty
  "SELF-CONFIDENCE",      # Assurance ↔ Insecurity
  "CONSISTENCY",          # Capriciousness ↔ Stability
  "MODESTY",              # Hubris ↔ Humility
  "RESILIENCE",           # Fragility ↔ Strength
  "APPRECIATION",         # Entitlement ↔ Gratitude
  "GENTLENESS",           # Tenderness ↔ Harshness
  "EMOTIONAL EXPRESSION", # Expressivity ↔ Inhibition
  "SELF-ESTEEM",          # Confidence ↔ Self-Doubt
  "COURAGE",              # Timidity ↔ Bravery
  "EMPATHY",              # Sociopathy ↔ Empathy
  "SEXUALITY",            # Sensuality ↔ Asexuality
  "HAPPINESS",            # Joy ↔ Sadness
  "TRANQUILITY",          # Calmness ↔ Anxiety
  "OUTLOOK",              # Optimism ↔ Pessimism
  "SELF-CONTROL",         # Patience ↔ Impulsiveness
  "TRUSTWORTHINESS",      # Trust ↔ Suspicion
  "GENEROSITY",           # Altruism ↔ Selfishness
  "COMPASSION"            # Compassion ↔ Indifference
]

social_traits = [
  "CANDOR",               # Candor ↔ Deceptiveness
  "FLEXIBILITY",          # Stubbornness ↔ Flexibility
  "METICULOUSNESS",       # Meticulousness ↔ Carelessness
  "SELF-SUFFICIENCY",     # Fastidiousness ↔ Self-Sufficiency
  "LEADERSHIP",           # Leadership ↔ Followership
  "INDIVIDUALISM",        # Individualism ↔ Collectivism
  "COURTESY",             # Courtesy ↔ Rudeness
  "CONGENIALITY",         # Congeniality ↔ Hostility
  "CONSIDERATION",        # Consideration ↔ Disregard
  "TACTFULNESS",          # Brusqueness ↔ Tactfulness
  "FIGURATIVE THINKING",  # Literalism ↔ Figurative Thinking
  "PACIFISM",             # Bellicosity ↔ Pacifism
  "OPENNESS",             # Reserve ↔ Openness
  "GENTLENESS",           # Gentleness ↔ Harshness
  "LOYALTY",              # Loyalty ↔ Betrayal
  "SELF-SACRIFICE"        # Self-Preservation ↔ Self-Sacrifice
]

cognitive_traits = [
  "KNOWLEDGE EXPANSION",  # Bulk Apperception ↔ Ignorance
  "INNOVATION",           # Innovation ↔ Conventionality
  "APTITUDE",             # Facility ↔ Ineptitude
  "WISDOM",               # Wisdom ↔ Foolishness
  "EDUCATION",            # Education ↔ Ignorance
  "DECISIVENESS",         # Decisiveness ↔ Indecisiveness
  "INTUITION",            # Intuition ↔ Rationality
  "CURIOSITY"             # Curiosity ↔ Apathy
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
  "POSE AND GRACE",       # Rhythm ↔ Arrhythmia
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

personality_trait_order = [
  'emotional_traits',
  'social_traits',
  'cognitive_traits',
  'behavioral_traits',
  'moral_traits',
  'physical_health_traits',
  'communication_traits'
]

personality_traits = {
  'emotional_traits': emotional_traits,
  'social_traits': social_traits,
  'cognitive_traits': cognitive_traits,
  'behavioral_traits': behavioral_traits,
  'moral_traits': moral_traits,
  'physical_health_traits': physical_health_traits,
  'communication_traits': communication_traits
}
