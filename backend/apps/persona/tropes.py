# EXAMPLES OF OTHER TROPES
# HTTPS://THESCRIPTLAB.COM/BLOGS/40182-101-CHARACTER-TROPES/

import random

def get_random_trope():
    tropes = get_personality_tropes()
    return random.choice(list(tropes.keys()))


def get_personality_tropes():
    return {
        "THE_LEADER": {
            "emotional": {
                "RECONCILIATION": 6, "BENEVOLENCE": 7, "SELF-CONFIDENCE": 9, "CONSISTENCY": 8, "MODESTY": 6,
                "RESILIENCE": 9, "APPRECIATION": 7, "GENTLENESS": 6, "EMOTIONAL_EXPRESSION": 7, "SELF-ESTEEM": 9,
                "COURAGE": 9, "EMPATHY": 7, "SEXUALITY": 6, "HAPPINESS": 7, "ANGER": 5, "TRANQUILITY": 6,
                "OUTLOOK": 8, "SELF-CONTROL": 8, "TRUSTWORTHINESS": 9, "GENEROSITY": 7, "COMPASSION": 7
            },
            "social": {
                "KINDNESS": 7, "FRIENDLINESS": 8, "CONFIDENCE": 9, "CHARISMA": 8, "EMPATHY": 7,
                "LOYALTY": 9, "COMPASSION": 7, "ALTRUISM": 8
            },
            "cognitive": {
                "KNOWLEDGE": 8, "INNOVATION": 7, "APTITUDE": 8, "WISDOM": 8, "EDUCATION": 8,
                "DECISIVENESS": 9, "INTUITION": 7, "CURIOSITY": 7, "MEMORY": 8
            },
            "behavioral": {
                "COORDINATION": 8, "INDUSTRY": 9, "WHIMSY": 6, "EXTROVERSION": 8,
                "COMPETITIVENESS": 8, "WANDERLUST": 6, "TENACITY": 9
            },
            "physical_health": {
                "POSE_AND_GRACE": 8, "FASHIONABLENESS": 7, "STRENGTH": 8
            },
            "moral": {
                "INTEGRITY": 9, "MORALITY": 8, "FIDELITY": 9, "SPIRITUALITY": 7, "FAITH": 7,
                "PATRIOTISM": 8, "HUMILITY": 6, "HUMOR": 7, "SINCERITY": 8
            }
        },
        "THE_CAREGIVER": {
            "emotional": {
                "RECONCILIATION": 8, "BENEVOLENCE": 9, "SELF-CONFIDENCE": 6, "CONSISTENCY": 7, "MODESTY": 8,
                "RESILIENCE": 7, "APPRECIATION": 9, "GENTLENESS": 9, "EMOTIONAL_EXPRESSION": 8, "SELF-ESTEEM": 6,
                "COURAGE": 7, "EMPATHY": 9, "SEXUALITY": 6, "HAPPINESS": 8, "ANGER": 4, "TRANQUILITY": 7,
                "OUTLOOK": 8, "SELF-CONTROL": 8, "TRUSTWORTHINESS": 9, "GENEROSITY": 9, "COMPASSION": 9
            },
            "social": {
                "KINDNESS": 9, "FRIENDLINESS": 8, "CONFIDENCE": 6, "CHARISMA": 7, "EMPATHY": 9,
                "LOYALTY": 9, "COMPASSION": 9, "ALTRUISM": 9
            },
            "cognitive": {
                "KNOWLEDGE": 7, "INNOVATION": 6, "APTITUDE": 7, "WISDOM": 8, "EDUCATION": 7,
                "DECISIVENESS": 6, "INTUITION": 8, "CURIOSITY": 7, "MEMORY": 7
            },
            "behavioral": {
                "COORDINATION": 7, "INDUSTRY": 8, "WHIMSY": 7, "EXTROVERSION": 8,
                "COMPETITIVENESS": 5, "WANDERLUST": 6, "TENACITY": 8
            },
            "physical_health": {
                "POSE_AND_GRACE": 7, "FASHIONABLENESS": 6, "STRENGTH": 7
            },
            "moral": {
                "INTEGRITY": 9, "MORALITY": 9, "FIDELITY": 9, "SPIRITUALITY": 8, "FAITH": 8,
                "PATRIOTISM": 7, "HUMILITY": 8, "HUMOR": 7, "SINCERITY": 9
            }
        },
        "THE_ADVENTURER": {
            "emotional": {
                "RECONCILIATION": 5, "BENEVOLENCE": 6, "SELF-CONFIDENCE": 8, "CONSISTENCY": 5, "MODESTY": 6,
                "RESILIENCE": 8, "APPRECIATION": 7, "GENTLENESS": 6, "EMOTIONAL_EXPRESSION": 8, "SELF-ESTEEM": 8,
                "COURAGE": 9, "EMPATHY": 7, "SEXUALITY": 7, "HAPPINESS": 8, "ANGER": 5, "TRANQUILITY": 6,
                "OUTLOOK": 8, "SELF-CONTROL": 7, "TRUSTWORTHINESS": 7, "GENEROSITY": 7, "COMPASSION": 7
            },
            "social": {
                "KINDNESS": 6, "FRIENDLINESS": 8, "CONFIDENCE": 8, "CHARISMA": 7, "EMPATHY": 7,
                "LOYALTY": 7, "COMPASSION": 7, "ALTRUISM": 7
            },
            "cognitive": {
                "KNOWLEDGE": 7, "INNOVATION": 8, "APTITUDE": 7, "WISDOM": 7, "EDUCATION": 7,
                "DECISIVENESS": 8, "INTUITION": 8, "CURIOSITY": 9, "MEMORY": 7
            },
            "behavioral": {
                "COORDINATION": 8, "INDUSTRY": 7, "WHIMSY": 8, "EXTROVERSION": 8,
                "COMPETITIVENESS": 7, "WANDERLUST": 9, "TENACITY": 8
            },
            "physical_health": {
                "POSE_AND_GRACE": 8, "FASHIONABLENESS": 7, "STRENGTH": 8
            },
            "moral": {
                "INTEGRITY": 8, "MORALITY": 7, "FIDELITY": 8, "SPIRITUALITY": 7, "FAITH": 7,
                "PATRIOTISM": 8, "HUMILITY": 7, "HUMOR": 8, "SINCERITY": 8
            }
        },
        "THE_SCHOLAR": {
            "emotional": {
                "RECONCILIATION": 6, "BENEVOLENCE": 7, "SELF-CONFIDENCE": 6, "CONSISTENCY": 8, "MODESTY": 7,
                "RESILIENCE": 7, "APPRECIATION": 7, "GENTLENESS": 7, "EMOTIONAL_EXPRESSION": 5, "SELF-ESTEEM": 6,
                "COURAGE": 6, "EMPATHY": 7, "SEXUALITY": 5, "HAPPINESS": 7, "ANGER": 4, "TRANQUILITY": 8,
                "OUTLOOK": 7, "SELF-CONTROL": 8, "TRUSTWORTHINESS": 8, "GENEROSITY": 7, "COMPASSION": 7
            },
            "social": {
                "KINDNESS": 7, "FRIENDLINESS": 6, "CONFIDENCE": 6, "CHARISMA": 6, "EMPATHY": 7,
                "LOYALTY": 8, "COMPASSION": 7, "ALTRUISM": 7
            },
            "cognitive": {
                "KNOWLEDGE": 9, "INNOVATION": 8, "APTITUDE": 8, "WISDOM": 9, "EDUCATION": 9,
                "DECISIVENESS": 7, "INTUITION": 8, "CURIOSITY": 9, "MEMORY": 8
            },
            "behavioral": {
                "COORDINATION": 6, "INDUSTRY": 8, "WHIMSY": 6, "EXTROVERSION": 5,
                "COMPETITIVENESS": 7, "WANDERLUST": 6, "TENACITY": 8
            },
            "physical_health": {
                "POSE_AND_GRACE": 6, "FASHIONABLENESS": 5, "STRENGTH": 6
            },
            "moral": {
                "INTEGRITY": 8, "MORALITY": 8, "FIDELITY": 8, "SPIRITUALITY": 7, "FAITH": 7,
                "PATRIOTISM": 7, "HUMILITY": 7, "HUMOR": 6, "SINCERITY": 8
            }
        },
        "THE_ARTIST": {
            "emotional": {
                "RECONCILIATION": 7, "BENEVOLENCE": 8, "SELF-CONFIDENCE": 7, "CONSISTENCY": 6, "MODESTY": 6,
                "RESILIENCE": 7, "APPRECIATION": 8, "GENTLENESS": 8, "EMOTIONAL_EXPRESSION": 9, "SELF-ESTEEM": 7,
                "COURAGE": 7, "EMPATHY": 8, "SEXUALITY": 7, "HAPPINESS": 8, "ANGER": 4, "TRANQUILITY": 7,
                "OUTLOOK": 8, "SELF-CONTROL": 7, "TRUSTWORTHINESS": 7, "GENEROSITY": 8, "COMPASSION": 8
            },
            "social": {
                "KINDNESS": 8, "FRIENDLINESS": 8, "CONFIDENCE": 7, "CHARISMA": 8, "EMPATHY": 8,
                "LOYALTY": 7, "COMPASSION": 8, "ALTRUISM": 8
            },
            "cognitive": {
                "KNOWLEDGE": 7, "INNOVATION": 9, "APTITUDE": 8, "WISDOM": 7, "EDUCATION": 7,
                "DECISIVENESS": 6, "INTUITION": 9, "CURIOSITY": 8, "MEMORY": 7
            },
            "behavioral": {
                "COORDINATION": 7, "INDUSTRY": 7, "WHIMSY": 9, "EXTROVERSION": 7,
                "COMPETITIVENESS": 6, "WANDERLUST": 7, "TENACITY": 7
            },
            "physical_health": {
                "POSE_AND_GRACE": 7, "FASHIONABLENESS": 8, "STRENGTH": 6
            },
            "moral": {
                "INTEGRITY": 8, "MORALITY": 7, "FIDELITY": 7, "SPIRITUALITY": 8, "FAITH": 7,
                "PATRIOTISM": 7, "HUMILITY": 7, "HUMOR": 8, "SINCERITY": 8
            }
        },
        "THE_LONER": {
            "emotional": {
                "RECONCILIATION": 3, "BENEVOLENCE": 4, "SELF-CONFIDENCE": 3, "CONSISTENCY": 5, "MODESTY": 6,
                "RESILIENCE": 4, "APPRECIATION": 3, "GENTLENESS": 4, "EMOTIONAL_EXPRESSION": 3, "SELF-ESTEEM": 3,
                "COURAGE": 4, "EMPATHY": 3, "SEXUALITY": 4, "HAPPINESS": 3, "ANGER": 6, "TRANQUILITY": 4,
                "OUTLOOK": 4, "SELF-CONTROL": 5, "TRUSTWORTHINESS": 3, "GENEROSITY": 4, "COMPASSION": 3
            },
            "social": {
                "KINDNESS": 4, "FRIENDLINESS": 3, "CONFIDENCE": 3, "CHARISMA": 3, "EMPATHY": 3,
                "LOYALTY": 4, "COMPASSION": 3, "ALTRUISM": 3
            },
            "cognitive": {
                "KNOWLEDGE": 5, "INNOVATION": 4, "APTITUDE": 5, "WISDOM": 5, "EDUCATION": 5,
                "DECISIVENESS": 3, "INTUITION": 4, "CURIOSITY": 4, "MEMORY": 5
            },
            "behavioral": {
                "COORDINATION": 4, "INDUSTRY": 4, "WHIMSY": 3, "EXTROVERSION": 2,
                "COMPETITIVENESS": 4, "WANDERLUST": 3, "TENACITY": 4
            },
            "physical_health": {
                "POSE_AND_GRACE": 4, "FASHIONABLENESS": 3, "STRENGTH": 4
            },
            "moral": {
                "INTEGRITY": 4, "MORALITY": 4, "FIDELITY": 4, "SPIRITUALITY": 5, "FAITH": 4,
                "PATRIOTISM": 4, "HUMILITY": 5, "HUMOR": 3, "SINCERITY": 4
            }
        },
        "THE_FOLLOWER": {
            "emotional": {
                "RECONCILIATION": 5, "BENEVOLENCE": 5, "SELF-CONFIDENCE": 4, "CONSISTENCY": 6, "MODESTY": 5,
                "RESILIENCE": 5, "APPRECIATION": 5, "GENTLENESS": 5, "EMOTIONAL_EXPRESSION": 5, "SELF-ESTEEM": 4,
                "COURAGE": 4, "EMPATHY": 5, "SEXUALITY": 4, "HAPPINESS": 5, "ANGER": 5, "TRANQUILITY": 5,
                "OUTLOOK": 5, "SELF-CONTROL": 5, "TRUSTWORTHINESS": 5, "GENEROSITY": 5, "COMPASSION": 5
            },
            "social": {
                "KINDNESS": 5, "FRIENDLINESS": 5, "CONFIDENCE": 4, "CHARISMA": 5, "EMPATHY": 5,
                "LOYALTY": 6, "COMPASSION": 5, "ALTRUISM": 5
            },
            "cognitive": {
                "KNOWLEDGE": 5, "INNOVATION": 4, "APTITUDE": 5, "WISDOM": 5, "EDUCATION": 5,
                "DECISIVENESS": 4, "INTUITION": 5, "CURIOSITY": 4, "MEMORY": 5
            },
            "behavioral": {
                "COORDINATION": 5, "INDUSTRY": 5, "WHIMSY": 4, "EXTROVERSION": 4,
                "COMPETITIVENESS": 4, "WANDERLUST": 4, "TENACITY": 5
            },
            "physical_health": {
                "POSE_AND_GRACE": 5, "FASHIONABLENESS": 4, "STRENGTH": 5
            },
            "moral": {
                "INTEGRITY": 5, "MORALITY": 5, "FIDELITY": 5, "SPIRITUALITY": 5, "FAITH": 5,
                "PATRIOTISM": 5, "HUMILITY": 5, "HUMOR": 5, "SINCERITY": 5
            }
        },
        "THE_FLIRT": {
            "emotional": {
                "RECONCILIATION": 5, "BENEVOLENCE": 6, "SELF-CONFIDENCE": 8, "CONSISTENCY": 5, "MODESTY": 4,
                "RESILIENCE": 6, "APPRECIATION": 6, "GENTLENESS": 7, "EMOTIONAL_EXPRESSION": 8, "SELF-ESTEEM": 8,
                "COURAGE": 6, "EMPATHY": 6, "SEXUALITY": 9, "HAPPINESS": 7, "ANGER": 4, "TRANQUILITY": 6,
                "OUTLOOK": 7, "SELF-CONTROL": 5, "TRUSTWORTHINESS": 5, "GENEROSITY": 6, "COMPASSION": 6
            },
            "social": {
                "KINDNESS": 6, "FRIENDLINESS": 9, "CONFIDENCE": 8, "CHARISMA": 9, "EMPATHY": 6,
                "LOYALTY": 5, "COMPASSION": 6, "ALTRUISM": 5
            },
            "cognitive": {
                "KNOWLEDGE": 5, "INNOVATION": 6, "APTITUDE": 6, "WISDOM": 5, "EDUCATION": 6,
                "DECISIVENESS": 6, "INTUITION": 7, "CURIOSITY": 6, "MEMORY": 6
            },
            "behavioral": {
                "COORDINATION": 7, "INDUSTRY": 5, "WHIMSY": 7, "EXTROVERSION": 9,
                "COMPETITIVENESS": 6, "WANDERLUST": 6, "TENACITY": 6
            },
            "physical_health": {
                "POSE_AND_GRACE": 8, "FASHIONABLENESS": 8, "STRENGTH": 6
            },
            "moral": {
                "INTEGRITY": 5, "MORALITY": 5, "FIDELITY": 4, "SPIRITUALITY": 5, "FAITH": 5,
                "PATRIOTISM": 5, "HUMILITY": 5, "HUMOR": 7, "SINCERITY": 6
            }
        },
        "THE_OPTIMIST": {
            "emotional": {
                "RECONCILIATION": 8, "BENEVOLENCE": 8, "SELF-CONFIDENCE": 7, "CONSISTENCY": 7, "MODESTY": 6,
                "RESILIENCE": 8, "APPRECIATION": 8, "GENTLENESS": 8, "EMOTIONAL_EXPRESSION": 7, "SELF-ESTEEM": 7,
                "COURAGE": 7, "EMPATHY": 7, "SEXUALITY": 6, "HAPPINESS": 9, "ANGER": 3, "TRANQUILITY": 8,
                "OUTLOOK": 9, "SELF-CONTROL": 8, "TRUSTWORTHINESS": 8, "GENEROSITY": 8, "COMPASSION": 8
            },
            "social": {
                "KINDNESS": 8, "FRIENDLINESS": 8, "CONFIDENCE": 7, "CHARISMA": 7, "EMPATHY": 8,
                "LOYALTY": 8, "COMPASSION": 8, "ALTRUISM": 8
            },
            "cognitive": {
                "KNOWLEDGE": 6, "INNOVATION": 7, "APTITUDE": 7, "WISDOM": 7, "EDUCATION": 7,
                "DECISIVENESS": 7, "INTUITION": 8, "CURIOSITY": 7, "MEMORY": 7
            },
            "behavioral": {
                "COORDINATION": 7, "INDUSTRY": 7, "WHIMSY": 8, "EXTROVERSION": 7,
                "COMPETITIVENESS": 6, "WANDERLUST": 7, "TENACITY": 8
            },
            "physical_health": {
                "POSE_AND_GRACE": 7, "FASHIONABLENESS": 7, "STRENGTH": 7
            },
            "moral": {
                "INTEGRITY": 8, "MORALITY": 8, "FIDELITY": 8, "SPIRITUALITY": 7, "FAITH": 7,
                "PATRIOTISM": 7, "HUMILITY": 7, "HUMOR": 8, "SINCERITY": 8
            }
        },
        "THE_INNOCENT": {
            "emotional": {
                "RECONCILIATION": 7, "BENEVOLENCE": 9, "SELF-CONFIDENCE": 5, "CONSISTENCY": 6, "MODESTY": 8,
                "RESILIENCE": 5, "APPRECIATION": 8, "GENTLENESS": 9, "EMOTIONAL_EXPRESSION": 6, "SELF-ESTEEM": 5,
                "COURAGE": 5, "EMPATHY": 8, "SEXUALITY": 4, "HAPPINESS": 8, "ANGER": 2, "TRANQUILITY": 7,
                "OUTLOOK": 8, "SELF-CONTROL": 7, "TRUSTWORTHINESS": 8, "GENEROSITY": 8, "COMPASSION": 8
            },
            "social": {
                "KINDNESS": 9, "FRIENDLINESS": 8, "CONFIDENCE": 5, "CHARISMA": 6, "EMPATHY": 8,
                "LOYALTY": 8, "COMPASSION": 8, "ALTRUISM": 8
            },
            "cognitive": {
                "KNOWLEDGE": 5, "INNOVATION": 5, "APTITUDE": 5, "WISDOM": 6, "EDUCATION": 6,
                "DECISIVENESS": 4, "INTUITION": 6, "CURIOSITY": 6, "MEMORY": 6
            },
            "behavioral": {
                "COORDINATION": 5, "INDUSTRY": 5, "WHIMSY": 7, "EXTROVERSION": 5,
                "COMPETITIVENESS": 4, "WANDERLUST": 6, "TENACITY": 5
            },
            "physical_health": {
                "POSE_AND_GRACE": 6, "FASHIONABLENESS": 5, "STRENGTH": 5
            },
            "moral": {
                "INTEGRITY": 8, "MORALITY": 8, "FIDELITY": 8, "SPIRITUALITY": 8, "FAITH": 8,
                "PATRIOTISM": 7, "HUMILITY": 8, "HUMOR": 7, "SINCERITY": 8
            }
        },
        "THE_VILLAIN": {
            "emotional": {
                "RECONCILIATION": 2, "BENEVOLENCE": 2, "SELF-CONFIDENCE": 8, "CONSISTENCY": 7, "MODESTY": 3,
                "RESILIENCE": 8, "APPRECIATION": 2, "GENTLENESS": 2, "EMOTIONAL_EXPRESSION": 5, "SELF-ESTEEM": 8,
                "COURAGE": 7, "EMPATHY": 2, "SEXUALITY": 6, "HAPPINESS": 3, "ANGER": 9, "TRANQUILITY": 3,
                "OUTLOOK": 3, "SELF-CONTROL": 7, "TRUSTWORTHINESS": 2, "GENEROSITY": 2, "COMPASSION": 2
            },
            "social": {
                "KINDNESS": 2, "FRIENDLINESS": 3, "CONFIDENCE": 8, "CHARISMA": 8, "EMPATHY": 2,
                "LOYALTY": 3, "COMPASSION": 2, "ALTRUISM": 2
            },
            "cognitive": {
                "KNOWLEDGE": 8, "INNOVATION": 7, "APTITUDE": 8, "WISDOM": 7, "EDUCATION": 7,
                "DECISIVENESS": 8, "INTUITION": 8, "CURIOSITY": 7, "MEMORY": 8
            },
            "behavioral": {
                "COORDINATION": 7, "INDUSTRY": 8, "WHIMSY": 5, "EXTROVERSION": 7,
                "COMPETITIVENESS": 9, "WANDERLUST": 6, "TENACITY": 8
            },
            "physical_health": {
                "POSE_AND_GRACE": 7, "FASHIONABLENESS": 7, "STRENGTH": 8
            },
            "moral": {
                "INTEGRITY": 2, "MORALITY": 2, "FIDELITY": 2, "SPIRITUALITY": 3, "FAITH": 3,
                "PATRIOTISM": 4, "HUMILITY": 3, "HUMOR": 4, "SINCERITY": 2
            }
        },
        "THE_FEMME_FATALE": {
            "emotional": {
                "RECONCILIATION": 3, "BENEVOLENCE": 3, "SELF-CONFIDENCE": 8, "CONSISTENCY": 6, "MODESTY": 4,
                "RESILIENCE": 7, "APPRECIATION": 4, "GENTLENESS": 3, "EMOTIONAL_EXPRESSION": 6, "SELF-ESTEEM": 8,
                "COURAGE": 7, "EMPATHY": 3, "SEXUALITY": 9, "HAPPINESS": 5, "ANGER": 6, "TRANQUILITY": 5,
                "OUTLOOK": 5, "SELF-CONTROL": 6, "TRUSTWORTHINESS": 3, "GENEROSITY": 3, "COMPASSION": 3
            },
            "social": {
                "KINDNESS": 3, "FRIENDLINESS": 7, "CONFIDENCE": 8, "CHARISMA": 9, "EMPATHY": 3,
                "LOYALTY": 3, "COMPASSION": 3, "ALTRUISM": 3
            },
            "cognitive": {
                "KNOWLEDGE": 7, "INNOVATION": 7, "APTITUDE": 7, "WISDOM": 6, "EDUCATION": 7,
                "DECISIVENESS": 7, "INTUITION": 8, "CURIOSITY": 7, "MEMORY": 7
            },
            "behavioral": {
                "COORDINATION": 7, "INDUSTRY": 6, "WHIMSY": 6, "EXTROVERSION": 8,
                "COMPETITIVENESS": 7, "WANDERLUST": 6, "TENACITY": 7
            },
            "physical_health": {
                "POSE_AND_GRACE": 8, "FASHIONABLENESS": 8, "STRENGTH": 6
            },
            "moral": {
                "INTEGRITY": 3, "MORALITY": 3, "FIDELITY": 3, "SPIRITUALITY": 4, "FAITH": 4,
                "PATRIOTISM": 4, "HUMILITY": 4, "HUMOR": 6, "SINCERITY": 3
            }
        },
        "THE_LOVABLE_ROGUE": {
            "emotional": {
                "RECONCILIATION": 5, "BENEVOLENCE": 5, "SELF-CONFIDENCE": 7, "CONSISTENCY": 5, "MODESTY": 5,
                "RESILIENCE": 7, "APPRECIATION": 6, "GENTLENESS": 6, "EMOTIONAL_EXPRESSION": 7, "SELF-ESTEEM": 7,
                "COURAGE": 8, "EMPATHY": 6, "SEXUALITY": 7, "HAPPINESS": 7, "ANGER": 5, "TRANQUILITY": 6,
                "OUTLOOK": 7, "SELF-CONTROL": 5, "TRUSTWORTHINESS": 4, "GENEROSITY": 5, "COMPASSION": 5
            },
            "social": {
                "KINDNESS": 5, "FRIENDLINESS": 8, "CONFIDENCE": 7, "CHARISMA": 8, "EMPATHY": 6,
                "LOYALTY": 6, "COMPASSION": 5, "ALTRUISM": 5
            },
            "cognitive": {
                "KNOWLEDGE": 6, "INNOVATION": 7, "APTITUDE": 7, "WISDOM": 6, "EDUCATION": 6,
                "DECISIVENESS": 6, "INTUITION": 7, "CURIOSITY": 7, "MEMORY": 6
            },
            "behavioral": {
                "COORDINATION": 7, "INDUSTRY": 6, "WHIMSY": 7, "EXTROVERSION": 8,
                "COMPETITIVENESS": 6, "WANDERLUST": 7, "TENACITY": 7
            },
            "physical_health": {
                "POSE_AND_GRACE": 7, "FASHIONABLENESS": 7, "STRENGTH": 7
            },
            "moral": {
                "INTEGRITY": 5, "MORALITY": 4, "FIDELITY": 5, "SPIRITUALITY": 5, "FAITH": 5,
                "PATRIOTISM": 6, "HUMILITY": 5, "HUMOR": 7, "SINCERITY": 5
            }
        }
    }
