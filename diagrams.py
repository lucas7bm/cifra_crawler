import pickle
from tonal_pitch_space import TonalPitchSpace
from pychord import Chord

def chords_and_distances(pitch):
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

def genres():
    filehandler = open('cifras.pickle', 'rb')
    cifras = pickle.load(filehandler)
    cifras = [x.__getitem__(0) for x in cifras]

    genres_array = []
    for x in cifras:
        exists_genre = False
        for tuple in genres_array:
            if x.genre == tuple.__getitem__(0):
                tuple.__getitem__(1).append(x.url)
                exists_genre = True

        if not exists_genre:
            genres_array.append((x.genre, [x.url]))

    for tuple in sorted(genres_array):
        print(tuple.__getitem__(0), ":", len(tuple.__getitem__(1)))

    print("Total of ", len(genres_array), " genres.")

def artists():
    filehandler = open('cifras.pickle', 'rb')
    cifras = pickle.load(filehandler)
    cifras = [x.__getitem__(0) for x in cifras]

    artist_array = []
    for x in cifras:
        exists_artist = False
        for tuple in artist_array:
            if x.artist == tuple.__getitem__(0):
                tuple.__getitem__(1).append(x.url)
                exists_artist = True

        if not exists_artist:
            artist_array.append((x.artist, [x.url]))
    print("Total of ", len(artist_array), " artists.")
    # for tuple in sorted(artist_array):
    #     print(tuple.__getitem__(0), ":", len(tuple.__getitem__(1)))

#chords_and_distances("C")
genres()
print()
artists()