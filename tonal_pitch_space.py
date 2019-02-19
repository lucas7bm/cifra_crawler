from pychord import Chord
from pychord.utils import note_to_val, val_to_note
from pychord.constants.scales import MAJOR_SCALE, MINOR_SCALE

class TonalPitchSpace:
    """ Classe representando um Tonal Pitch Space de Lerdahl

    :param str root: A raiz do acorde cujo campo harmônico vai gerar o Tonal Pitch Space
    :param str quality: A qualidade desse campo harmônico (major/minor)
    :param [int] level_a: o nível a, contendo somente a raiz do acorde
    :param [int] level_b: o nível b, contendo a raiz e a quinta do acorde
    :param [int] level_c: o nível triádico, contendo todas as notas do acorde
    :param [int] level_d: o nível diatônico, contendo as notas da escala do campo harmônico atual

    """
    def __init__(self, chord):
        self.chord = chord

        self.level_a = [chord.triad(False)[0]]
        print(self.level_a)
        self.level_b = [chord.triad(False)[0], chord.triad(False)[2]]
        print(self.level_b)
        self.level_c = [chord.triad(False)[0], chord.triad(False)[1], chord.triad(False)[2]]
        print(self.level_c)

        if(self.level_c[1] == (note_to_val(chord.root)+4) % 12):
            self.level_d = [(note_to_val(chord.root) + v) % 12 for v in MAJOR_SCALE]
            print(self.level_d)

        if(self.level_c[1] == (note_to_val(chord.root)+3) % 12):
            self.level_d = [(note_to_val(chord.root) + v) % 12 for v in MINOR_SCALE]
            print(self.level_d)

    def distance(self, chord):
        distance = 0

        distance += len(set(self.level_a) ^ set([chord.triad(False)[0]]))
        distance += len(set(self.level_b) ^ set([chord.triad(False)[0], chord.triad(False)[2]]))
        distance += len(set(self.level_c) ^ set([chord.triad(False)[0], chord.triad(False)[1], chord.triad(False)[2]]))
        print("Comp: ", chord.components(False))
        print(set(v % 12 for v in chord.components(False)))
        distance += len(set(self.level_c) ^ set(v % 12 for v in chord.components(False)))

        return distance

chd = TonalPitchSpace(Chord("C"))
print("Dist: ", chd.distance(Chord("G7")))
#chd2 = TonalPitchSpace(Chord("Cm"))
print()
#chd = TonalPitchSpace(Chord("B"))
chd2 = TonalPitchSpace(Chord("D"))
print()
#chd = TonalPitchSpace(Chord("D"))
#chd2 = TonalPitchSpace(Chord("Dm"))

print(set(chd.level_a) ^ set(chd2.level_a))