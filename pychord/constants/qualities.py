# -*- coding, utf-8 -*-

from collections import OrderedDict

QUALITY_DICT = OrderedDict((
    # 3 notes
    ('', [0, 4, 7]),
    ('maj', [0, 4, 7]),
    ('m', [0, 3, 7]),
    ('min', [0, 3, 7]),
    ('dim', [0, 3, 6]),
    ('dim7', [0, 3, 6, 10]),
    ('aug', [0, 4, 8]),
    ('+', [0, 4, 8]),
    ('5+', [0, 4, 8]),
    ('m5+', [0, 3, 8]),
    ('5-', [0, 4, 6]),
    ('m5-', [0, 3, 6]),
    ('5b', [0, 4, 6]),
    ('m5b', [0, 3, 6]),
    ('5-', [0, 4, 6]),
    ('m5-', [0, 3, 6]),
    ('sus2', [0, 2, 7]),
    ('sus4', [0, 5, 7]),
    ('sus', [0, 5, 7]),
    ('4', [0, 5, 7]),
    ('4+', [0, 4, 6]),
    ('m4+', [0, 3, 6]),
    # 4 notes
    ('m7b5', [0, 3, 6, 10]),
    ('7b5', [0, 3, 6, 10]),

    ('6', [0, 4, 7, 9]),
    ('m6', [0, 3, 7, 9]),

    ('(b6)', [0, 4, 7, 8]),
    ('m(b6)', [0, 3, 7, 8]),

    ('7', [0, 4, 7, 10]),
    ('7m', [0, 4, 7, 10]),
    ('m7', [0, 3, 7, 10]),

    ('7sus', [0, 5, 7, 10]),
    ('7(4)', [0, 5, 7, 10]),
    ('4(7)', [0, 5, 7, 10]),

    ('7(5b)', [0, 4, 6, 10]),
    ('m7(5b)', [0, 3, 6, 10]),

    ('7(b5)', [0, 4, 6, 10]),
    ('m7(b5)', [0, 3, 6, 10]),

    ('7(5-)', [0, 4, 6, 10]),
    ('m7(5-)', [0, 3, 6, 10]),

    ('7(5+)', [0, 4, 8, 10]),
    ('m7(5+)', [0, 3, 8, 10]),

    ('7M', [0, 4, 7, 11]),
    ('m7M', [0, 3, 7, 11]),

    ('(7M)', [0, 4, 7, 11]),
    ('m(7M)', [0, 3, 7, 11]),

    ('7+', [0, 4, 7, 10]),
    ('m7+', [0, 3, 7, 10]),

    ('M7', [0, 4, 7, 11]),
    ('mM7', [0, 3, 7, 11]),

    ('maj7', [0, 4, 7, 11]),
    ('Maj7', [0, 4, 7, 11]),
    ('M7+5', [0, 4, 8, 11]),
    ('7-5', [0, 4, 6, 10]),
    ('7+5', [0, 4, 8, 10]),
    ('7sus4', [0, 5, 7, 10]),
    ('m7-5', [0, 3, 6, 10]),
    ('dim6', [0, 3, 6, 9]),
    ('°', [0, 3, 6, 9]),
    ('º', [0, 3, 6, 9]),
    ('°(b13)', [0, 3, 6, 8]),
    ('º(b13)', [0, 3, 6, 8]),

    ('add9', [0, 4, 7, 14]),
    ('madd9', [0, 3, 7, 14]),

    ('(add9)', [0, 4, 7, 14]),
    ('m(add9)', [0, 3, 7, 14]),

    ('2', [0, 4, 7, 14]),
    ('add11', [0, 4, 7, 17]),
    # 5 notes
    ('m6(9)', [0, 3, 7, 9, 14]),
    ('6(9)', [0, 4, 7, 9, 14]),

    ('m4(6)', [0, 3, 7, 17, 21]),
    ('4(6)', [0, 4, 7, 17, 21]),

    ('m9', [0, 3, 7, 10, 14]),
    ('9', [0, 4, 7, 14]),

    ('m9(11)', [0, 3, 7, 14, 17]),
    ('9(11)', [0, 4, 7, 14, 17]),

    ('9(4+)', [0, 4, 7, 14, 18]),
    ('m9(4+)', [0, 3, 7, 14, 18]),

    ('maj9', [0, 4, 7, 11, 14]),
    ('M9', [0, 4, 7, 11, 14]),

    ('7+(9)',  [0, 4, 7, 11, 14]),
    ('m7+(9)',  [0, 3, 7, 11, 14]),

    ('7M(9)', [0, 4, 7, 11, 14]),
    ('m7M(9)', [0, 3, 7, 11, 14]),

    ('7M(6)', [0, 4, 7, 9, 11]),
    ('m7M(6)', [0, 3, 7, 9, 11]),

    ('9sus4', [0, 5, 7, 10, 14]),

    ('7(9b)', [0, 4, 7, 10, 13]),
    ('m7(9b)', [0, 4, 7, 10, 13]),

    ('7-9', [0, 4, 7, 10, 13]),
    ('m7-9', [0, 3, 7, 10, 13]),

    ('7+9', [0, 4, 7, 10, 15]),
    ('m7+9', [0, 3, 7, 10, 15]),

    ('11', [0, 4, 7, 17]),
    ('m11', [0, 3, 7, 17]),
    ('m4', [0, 3, 7, 17]),

    ('m11+', [0, 3, 7, 18]),
    ('11+', [0, 4, 7, 18]),

    ('7+11', [0, 4, 7, 10, 18]),
    ('m7+11', [0, 3, 7, 10, 18]),

    ('7(#11)', [0, 4, 7, 10, 18]),
    ('m7(#11)', [0, 3, 7, 10, 18]),

    ('7-13', [0, 4, 7, 10, 20]),
    ('m7-13', [0, 3, 7, 10, 20]),

    ('7(b9)', [0, 4, 7, 10, 13]),
    ('m7(b9)', [0, 3, 7, 10, 13]),

    ('7(9-)', [0, 4, 7, 10, 13]),
    ('m7(9-)', [0, 3, 7, 10, 13]),

    ('7(9)', [0, 4, 7, 10, 14]),
    ('m7(9)', [0, 3, 7, 10, 14]),

    ('7(9+)', [0, 4, 7, 10, 15]),
    ('m7(9+)', [0, 3, 7, 10, 15]),

    ('7(#9)', [0, 4, 7, 10, 15]),
    ('m7(#9)', [0, 3, 7, 10, 15]),

    ('7(11)', [0, 4, 7, 10, 17]),
    ('m7(11)', [0, 3, 7, 10, 17]),

    ('7(11+)', [0, 4, 7, 10, 18]),
    ('m7(11+)', [0, 3, 7, 10, 18]),

    ('6(11+)', [0, 4, 7, 9, 18]),
    ('m6(11+)', [0, 3, 7, 9, 18]),

    ('7M(11+)', [0, 4, 7, 11, 18]),
    ('m7M(11+)', [0, 3, 7, 11, 18]),

    ('7(13)', [0, 4, 7, 10, 21]),
    ('m7(13)', [0, 3, 7, 10, 21]),

    ('7(b13)', [0, 4, 7, 10, 20]),
    ('m7(b13)', [0, 3, 7, 10, 20]),

    ('7(13-)', [0, 4, 7, 10, 20]),
    ('m7(13-)', [0, 3, 7, 10, 20]),

    ("E13-", [0, 4, 7, 20]),
    # 6 notes
    ('13', [0, 4, 7, 10, 14, 21]),
))
