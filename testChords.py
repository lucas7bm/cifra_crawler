from pychord import Chord, Quality

print("C: ", Chord("C").triad(False))
print("G: ", Chord("G").triad(False))
print("D: ", Chord("D").triad(False))
print("A: ", Chord("A").triad(False))
print("E: ", Chord("E").triad(False))
print("B: ", Chord("B").triad(False))
print("Gb: ", Chord("Gb").triad(False))
print("Db: ", Chord("Db").triad(False))
print("Ab: ", Chord("Ab").triad(False))
print("Eb: ", Chord("Eb").triad(False))
print("Bb: ", Chord("Bb").triad(False))
print("F: ", Chord("F").triad(False))
print()
print("Am: ", Chord("Am").triad(False))
print("Em: ", Chord("Em").triad(False))
print("Bm: ", Chord("Bm").triad(False))
print("F#m: ", Chord("F#m").triad(False))
print("C#m: ", Chord("C#m").triad(False))
print("G#m: ", Chord("G#m").triad(False))
print("Ebm: ", Chord("Ebm").triad(False))
print("Bbm: ", Chord("Bbm").triad(False))
print("Fm: ", Chord("Fm").triad(False))
print("Cm: ", Chord("Cm").triad(False))
print("Gm: ", Chord("Gm").triad(False))
print("Dm: ", Chord("Dm").triad(False))

#problematic_chords = []

#cifra = Cifra("https://www.cifraclub.com.br/caetano-veloso/baiao-da-penha/")
#for chord in cifra.present_chords:
#    try:
#        ch = Chord(chord)
#        print(chord, ": ", ch.components())
#    except:
#        problematic_chords.append(chord)
#        print("I see a ", chord, "chord, but I can't read it! :(")