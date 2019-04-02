from pychord import Chord
from pychord.utils import note_to_val, val_to_note
from pychord.constants.scales import MAJOR_SCALE, MINOR_SCALE, CIRCLE_MAJ, CIRCLE_MIN

NON_DIATONIC_CONSTANT = 3

class TonalPitchSpace:
    """ Class representing a Lerdahl's tonal pitch space

    :param Chord chord: The chord which generates the Pitch Space
    :param [int] level_a: Lerdahl's level a, containing only the root of the chord
    :param [int] level_b: level b, containing the root and the fifth
    :param [int] level_c: triadic level, containing all of the chord's notes
    :param [int] level_d: the diatonic level, containing the notes of the harmonic field (it's scale)

    """
    def __init__(self, chord):
        self.chord = chord

        self.level_a = [chord.triad(False)[0]]
        self.level_b = [chord.triad(False)[0], chord.triad(False)[2]]
        self.level_c = [chord.triad(False)[0], chord.triad(False)[1], chord.triad(False)[2]]

        if(self.chord.is_major()):
            self.level_d = [(note_to_val(chord.root) + v) % 12 for v in MAJOR_SCALE]
        else:
            self.level_d = [(note_to_val(chord.root) + v) % 12 for v in MINOR_SCALE]

    def distance(self, chord):
        distance = 0

        try:
            distance += len(set(self.level_a) ^ set([chord.triad(False)[0]]))
            distance += len(set(self.level_b) ^ set([chord.triad(False)[0], chord.triad(False)[2]]))
            distance += len(set(self.level_c) ^ set([chord.triad(False)[0], chord.triad(False)[1], chord.triad(False)[2]]))
            distance += set(chord.components(False)).difference(set(self.level_d)).__len__()

            if(set(chord.triad(False)).issubset(set(self.level_d)) == False):
                return distance + NON_DIATONIC_CONSTANT

            #if it gets here, then it's a diatonic chord and it's circle-of-fifths distance will be calculated
            #we divide the index by 12 to create a gambiarra in which same chords with different names return
            #the same index value, like "C#" and "Db"
            if (self.chord.is_major()):
                index = CIRCLE_MAJ.index(self.chord.chord) % 12
            else:
                index = CIRCLE_MIN.index(self.chord.chord) % 12
            for i in range(0, 2):
                # rotating clockwise in the circle of fifths
                if (set(chord.triad(False)).difference(set(Chord(CIRCLE_MAJ[(index + i) % 12]).triad(False))) == set()
                        or set(chord.triad(False)).difference(set(Chord(CIRCLE_MIN[(index + i) % 12]).triad(False))) == set()):

                    distance += i
                # rotating counterclockwise
                if (set(chord.triad(False)).difference(set(Chord(CIRCLE_MAJ[(index - i + 12) % 12]).triad(False))) == set()
                        or set(chord.triad(False)).difference(set(Chord(CIRCLE_MIN[(index - i + 12) % 12]).triad(False))) == set()):
                    distance += i

            #assuming that the distance between C and Am on the circle is not 0, but 1, since we have to go "down" one step
            if(self.chord.is_major() != chord.is_major()):
                distance += 1

            return distance
        except:
            print("Oops")
            return 0


#tests
# chd = TonalPitchSpace(Chord("Db"))
#
# print("Dist C: ", chd.distance(Chord("C")))
# print("Dist Dm: ", chd.distance(Chord("Dm")))
# print("Dist Em: ", chd.distance(Chord("Em")))
# print("Dist F: ", chd.distance(Chord("F")))
# print("Dist G: ", chd.distance(Chord("G")))
# print("Dist Am: ", chd.distance(Chord("Am")))
# print("Dist B: ", chd.distance(Chord("B")))
# print()
# print("Dist Cm: ", chd.distance(Chord("Cm")))
# print("Dist D: ", chd.distance(Chord("D")))
# print("Dist E: ", chd.distance(Chord("E")))
# print("Dist Fm: ", chd.distance(Chord("Fm")))
# print("Dist Gm: ", chd.distance(Chord("Gm")))
# print("Dist A: ", chd.distance(Chord("A")))
# print("Dist Bm: ", chd.distance(Chord("Bm")))
# print()
#
# print("Dist minor: ", chd.distance(Chord("Dbm")))
# print("Dist same: ", chd.distance(Chord("C#")))
