import time
import traceback

from test_database import TEST_DATABASE, TDB
from cifra import Cifra

#problematic_chords = []

#cifra = Cifra("https://www.cifraclub.com.br/caetano-veloso/baiao-da-penha/")
#for chord in cifra.present_chords:
#    try:
#        ch = Chord(chord)
#        print(chord, ": ", ch.components())
#    except:
#        problematic_chords.append(chord)
#        print("I see a ", chord, "chord, but I can't read it! :(")

#i=0
#for x in TEST_DATABASE:
#    if(x.__getitem__(0) != ""):
#        i += 1
#        print(i, ": ", x.__getitem__(0))

less_than_seven = []
eight_to_twelve = []
thirteen_to_twenty = []
more_than_twenty = []

start_time = time.time()

test_data = []
record_of_chords = 0
less_chords = 100

for x in TEST_DATABASE:
    if(x.__getitem__(0) != ""):
        try:
            cifra = Cifra(x.__getitem__(0))
            test_data.append((cifra, x.__getitem__(1)))

            if cifra.present_chords.__len__() > record_of_chords:
                most_complex_song = cifra
                record_of_chords = cifra.present_chords.__len__()

            if cifra.present_chords.__len__() < less_chords:
                less_complex_song = cifra
                less_chords = cifra.present_chords.__len__()

            # Criando as categorias de complexidade
            if cifra.present_chords.__len__() > 20:
                more_than_twenty.append(cifra)
                continue
            if cifra.present_chords.__len__() > 12:
                thirteen_to_twenty.append(cifra)
                continue
            if cifra.present_chords.__len__() > 7:
                eight_to_twelve.append(cifra)
                continue
            else:
                less_than_seven.append(cifra)
        except:
            print("Cifra com problemas: ", x.__getitem__(0))
            traceback.print_exc()

#now lets tezt dis boi
incorrectly_analyzed = []
for x in test_data:
    if (x.__getitem__(0).found_tone == x.__getitem__(1)):
        print("yahoo!")
    else:
        incorrectly_analyzed.append(x)
        print("boooo :( ---> Found: ", x.__getitem__(0).found_tone,
              ". Given: ", x.__getitem__(0).given_tone,
              ". Tone: ", x.__getitem__(1))
        print(x.__getitem__(0).fields_distances)
        print(x.__getitem__(0).problematic_chords)
        print(x.__getitem__(0).url)

#print("Cifra mais complexa: ", most_complex_song.url, ", com ", record_of_chords, " acordes.")
#print(most_complex_song.problematic_chords)

print("\n\n>20: ", more_than_twenty.__len__())
print("13-20: ", thirteen_to_twenty.__len__())
print("8-12: ", eight_to_twelve.__len__())
print("<7: ", less_than_seven.__len__())

print("\n\n>20: ", [cifra.url for cifra in more_than_twenty])
print("13-20: ", [cifra.url for cifra in thirteen_to_twenty])
print("8-12: ", [cifra.url for cifra in eight_to_twelve])
print("<7: ", [cifra.url for cifra in less_than_seven])

#values = [0] * 50
#for x in test_data:
#    values[x.__getitem__(0).present_chords.__len__()] += 1
#
#print(values)

print("Success rate: ", 100.00 - ((incorrectly_analyzed.__len__() / test_data.__len__()) * 100.00))

print("--- %s seconds ---" % (time.time() - start_time))
