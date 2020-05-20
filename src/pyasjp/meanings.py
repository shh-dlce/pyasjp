__all__ = ['MEANINGS', 'MEANINGS_ALL', 'MEANINGS_NON_CORE']

MEANINGS = {
    1: ['I', 'je', 'ego', 'yo'],
    2: ['you', 'tú', 'tu', 'thou', 'tu, vos'],
    3: ['we', 'nous', 'nosotros', 'we two', 'nos', 'we (incl.)'],
    11: ['one', 'uno', 'un', 'unus'],
    12: ['two', 'deux', 'duo', 'dos'],
    18: ['person', 'personne', 'persona', 'homo, quidam'],
    19: ['fish', 'poisson', 'pez', 'fisx', 'piscis'],
    21: ['dog', 'perro', 'canis', 'chien'],
    22: ['louse', 'piojo', 'pediculus', 'pou'],
    23: ['tree', 'arbor', 'arbre', 'árbol', 'arbol'],
    25: ['leaf', 'folium', 'hoja', 'feuille'],
    28: ['skin', 'peaux', 'cutis, pellis', 'piel', 'peau'],
    30: ['blood', 'sangre', 'sang', 'sanguis'],
    31: ['bone', 'os', '%bone', 'hueso'],
    34: ['horn', 'corne', 'cuerno'],
    39: ['ear', 'oreille', 'oreja', 'auris'],
    40: ['eye', 'ojo', 'oculus', 'oeil'],
    41: ['nose', 'nariz', 'nez', 'nasus, nares'],
    43: ['tooth', 'dent', 'diente', 'dens'],
    44: ['tongue', 'lingua', 'lengua', 'langue'],
    47: ['knee', 'rodilla', 'genou', 'genu'],
    48: ['hand', 'main', 'mano', 'manus'],
    51: ['breast', 'breasts', 'seno', 'sein', 'mamma'],
    53: ['liver', 'higado', 'liverp', 'hígado', 'el higado', 'foie'],
    54: ['drink', 'boire', 'drinK', 'beber', 'bibere, potare', 'dring'],
    57: ['see', 'voir', 'ver'],
    58: ['hear', 'oir', 'oír', 'audire, exaudire', 'entendre', 'to hear'],
    61: ['die', 'morir', 'mourir', 'mori, obire'],
    66: ['come', 'venire', 'venir'],
    72: ['sun', 'soleil', 'sol'],
    74: ['star', 'etoile', 'estrella', 'stella, sidus'],
    75: ['water', 'eau', 'agua', 'aqua'],
    77: ['stone', 'piedra', 'pierre', 'lapis, saxum'],
    82: ['fire', 'firek', 'ignis', 'feu', 'fuego'],
    85: ['path', 'camino', 'semitas, trames, via', 'route', 'road', 'sendero'],
    86: ['mountain', 'mons', 'montagne', 'cerro', 'montaña', 'moundain'],
    92: ['night', 'noche', 'nuit'],
    95: ['full', 'full(ness)', 'lleno/a', 'plenus', 'lleno', 'plein'],
    96: ['new', 'nouveaux', 'nuevo'],
    100: ['name', 'nombre', 'nom', 'name (noun)'],
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
MEANINGS_ALL.update({k: v[0] for k, v in MEANINGS.items()})
MEANINGS_ALL.update(MEANINGS_NON_CORE)
# Check consistency of the meanings:
assert set(MEANINGS_ALL.keys()) == set(range(1, 101))  # Keys are numbers from 1 to 100.
assert len(set(MEANINGS_ALL.values())) == 100  # Meaning labels are unique.
