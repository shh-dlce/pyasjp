__all__ = ['MEANINGS', 'MEANINGS_ALL', 'MEANINGS_NON_CORE']

MEANINGS = {
    1: 'I',
    2: 'you',
    3: 'we',
    11: 'one',
    12: 'two',
    18: 'person',
    19: 'fish',
    21: 'dog',
    22: 'louse',
    23: 'tree',
    25: 'leaf',
    28: 'skin',
    30: 'blood',
    31: 'bone',
    34: 'horn',
    39: 'ear',
    40: 'eye',
    41: 'nose',
    43: 'tooth',
    44: 'tongue',
    47: 'knee',
    48: 'hand',
    51: 'breast',
    53: 'liver',
    54: 'drink',
    57: 'see',
    58: 'hear',
    61: 'die',
    66: 'come',
    72: 'sun',
    74: 'star',
    75: 'water',
    77: 'stone',
    82: 'fire',
    85: 'path',
    86: 'mountain',
    92: 'night',
    95: 'full',
    96: 'new',
    100: 'name',
}

MEANINGS_NON_CORE = {
    4: 'this',
    5: 'that',
    6: 'who',
    7: 'what',
    8: 'not',
    9: 'all',
    10: 'many',
    13: 'big',
    14: 'long',
    15: 'small',
    16: 'woman',
    17: 'man',
    20: 'bird',
    24: 'seed',
    26: 'root',
    27: 'bark',
    29: 'flesh',
    32: 'grease',
    33: 'egg',
    35: 'tail',
    36: 'feather',
    37: 'hair',
    38: 'head',
    42: 'mouth',
    45: 'claw',
    46: 'foot',
    49: 'belly',
    50: 'neck',
    52: 'heart',
    55: 'eat',
    56: 'bite',
    59: 'know',
    60: 'sleep',
    62: 'kill',
    63: 'swim',
    64: 'fly',
    65: 'walk',
    67: 'lie',
    68: 'sit',
    69: 'stand',
    70: 'give',
    71: 'say',
    73: 'moon',
    76: 'rain',
    78: 'sand',
    79: 'earth',
    80: 'cloud',
    81: 'smoke',
    83: 'ash',
    84: 'burn',
    87: 'red',
    88: 'green',
    89: 'yellow',
    90: 'white',
    91: 'black',
    93: 'hot',
    94: 'cold',
    97: 'good',
    98: 'round',
    99: 'dry',
}

MEANINGS_ALL = {}
MEANINGS_ALL.update(MEANINGS)
MEANINGS_ALL.update(MEANINGS_NON_CORE)
# Check consistency of the meanings:
assert list(MEANINGS_ALL.keys()) == list(range(1, 101))  # Keys are numbers from 1 to 100.
assert len(set(MEANINGS_ALL.values())) == 100  # Meaning labels are unique.
