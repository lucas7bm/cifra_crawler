from pychord2 import Chord, Quality
from cifra import Cifra

ch = Chord("G#dim/4")
print("Letter: ", ch.components())
print("Triad: ", ch.triad())

ch = Chord("Fmaj7/5")
print("Number: ", ch.components())

#problematic_chords = []

#cifra = Cifra("https://www.cifraclub.com.br/caetano-veloso/baiao-da-penha/")
#for chord in cifra.present_chords:
#    try:
#        ch = Chord(chord)
#        print(chord, ": ", ch.components())
#    except:
#        problematic_chords.append(chord)
#        print("I see a ", chord, "chord, but I can't read it! :(")