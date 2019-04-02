from pychord import Chord, Quality

#problematic_chords = []

#cifra = Cifra("https://www.cifraclub.com.br/caetano-veloso/baiao-da-penha/")
#for chord in cifra.present_chords:
#    try:
#        ch = Chord(chord)
#        print(chord, ": ", ch.components())
#    except:
#        problematic_chords.append(chord)
#        print("I see a ", chord, "chord, but I can't read it! :(")

print(Chord("C/B").root)