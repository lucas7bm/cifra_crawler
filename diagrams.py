import pickle
from tonal_pitch_space import TonalPitchSpace
from pychord import Chord

def tps_venn(pitch):
    filehandler = open('cifras.pickle', 'rb')
    cifras = pickle.load(filehandler)
    chords = []
    for cifra in cifras:
        for chord in cifra.__getitem__(0).parsed_chords:
            chords.append(chord.chord)
    chords = set(chords)
    print(len(chords))

    tps = TonalPitchSpace(Chord(pitch))

    chordal_distances = []

    for chord in chords:
        chr = Chord(chord)
        dist =  tps.distance(chr)

        exists = False
        for tuple in chordal_distances:
            if dist == tuple.__getitem__(0):
                aux = False
                for x in tuple.__getitem__(1):
                    if set(x.components()) == set(Chord(chord).components()):
                        aux = True
                        break
                if not aux:
                    tuple.__getitem__(1).append(Chord(chord))
                exists = True
                break

        if not exists:
            chordal_distances.append((dist, [Chord(chord)]))

    for x in (chordal_distances):
        for y in x.__getitem__(1):
            if y.components(False).__len__() == 3:
                if y.chord.find("/") != -1:
                    idx = y.chord.find("/")
                    y._chord = y._chord[:idx]


    for x in sorted(chordal_distances):
        print(x.__getitem__(0), ":\t ", [v.chord for v in x.__getitem__(1)])

tps_venn("C")