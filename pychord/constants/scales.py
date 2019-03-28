MAJOR_SCALE = {
    0, 2, 4, 5, 7, 9, 11
}

MINOR_SCALE = {
    0, 2, 3, 5, 7, 8, 10
}

NOTE_VAL_DICT = {
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11,
    'Cb': 11,
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
}

HARMONIC_FIELDS = {
    0: "C",
    0: "Cm",
    0: "D",
    0: "Dm",
    0: "E",
    0: "Em",
    0: "F",
    0: "Fm",
    0: "G",
    0: "Gm",
    0: "A",
    0: "Am",
    0: "B",
    0: "Bm",
}

VAL_NOTE_DICT = {
    0: ['C'],
    1: ['Db', 'C#'],
    2: ['D'],
    3: ['Eb', 'D#'],
    4: ['E'],
    5: ['F'],
    6: ['F#', 'Gb'],
    7: ['G'],
    8: ['Ab', 'G#'],
    9: ['A'],
    10: ['Bb', 'A#'],
    11: ['B', 'Cb']
}

INTERVAL_DICT = {
    '4':5,

    '4+':6,

    '-5':6,
    '5-':6,
    'b5':6,
    '5b':6,

    '5':7,

    '5+':8,
    '5#':8,
    '#5':8,

    '6':9,
    '7':11,
    '9-':13,
    '9-':13,
    '9':14,
    '11':17,
    '13':21,
    '13-':20,
}

SHARPED_SCALE = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#',
    4: 'E', 5: 'F', 6: 'F#', 7: 'G',
    8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}

FLATTED_SCALE = {
    0: 'C', 1: 'Db', 2: 'D', 3: 'Eb',
    4: 'E', 5: 'F', 6: 'Gb', 7: 'G',
    8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B'
}

SCALE_VAL_DICT = {
    'Ab': FLATTED_SCALE,
    'A': SHARPED_SCALE,
    'A#': SHARPED_SCALE,
    'Bb': FLATTED_SCALE,
    'B': SHARPED_SCALE,
    'Cb': FLATTED_SCALE,
    'C': FLATTED_SCALE,
    'C#': SHARPED_SCALE,
    'Db': FLATTED_SCALE,
    'D': SHARPED_SCALE,
    'D#': SHARPED_SCALE,
    'Eb': FLATTED_SCALE,
    'E': SHARPED_SCALE,
    'F': FLATTED_SCALE,
    'F#': SHARPED_SCALE,
    'Gb': FLATTED_SCALE,
    'G': SHARPED_SCALE,
    'G#': SHARPED_SCALE,
}