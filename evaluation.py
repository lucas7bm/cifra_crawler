import time
import traceback

from test_database import TEST_DATABASE, TDB
from cifra import Cifra

def Evaluate(BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT):
    less_than_seven = []
    eight_to_twelve = []
    thirteen_to_twenty = []
    more_than_twenty = []

    start_time = time.time()

    test_data = []
    record_of_chords = 0
    less_chords = 100

    for x in TEST_DATABASE:
        if (x.__getitem__(0) != ""):
            try:
                cifra = Cifra(x.__getitem__(0), BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT)
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
                None
                #print("Cifra com problemas: ", x.__getitem__(0))
                #traceback.print_exc()

    probl_chords = []
    # now lets tezt dis boi
    incorrectly_analyzed = []
    for x in test_data:
        if (x.__getitem__(0).found_tone == x.__getitem__(1)):
            # print("yahoo!")
            None
        else:
            incorrectly_analyzed.append(x)
            #print(x.__getitem__(0).url, " --> Found: ", x.__getitem__(0).found_tone, ". Given: ", x.__getitem__(0).given_tone, ". Tone: ", x.__getitem__(1))
            #print(x.__getitem__(0).fields_distances)

            for chord in x.__getitem__(0).problematic_chords:
                probl_chords.append(chord)

    # print("Cifra mais complexa: ", most_complex_song.url, ", com ", record_of_chords, " acordes.")
    # print(most_complex_song.problematic_chords)

    #print("\n\n>20: ", more_than_twenty.__len__())
    #print("13-20: ", thirteen_to_twenty.__len__())
    #print("8-12: ", eight_to_twelve.__len__())
    #print("<7: ", less_than_seven.__len__())

    # values = [0] * 50
    # for x in test_data:
    #    values[x.__getitem__(0).present_chords.__len__()] += 1
    #
    # print(values)
    print("\n\n", BOTH_CONSTANT, " ", FIRST_CONSTANT, " ", LAST_CONSTANT)
    print("Success rate: ", 100.00 - ((incorrectly_analyzed.__len__() / test_data.__len__()) * 100.00))
    print("--- %s seconds ---" % (time.time() - start_time))
    return 100.00 - ((incorrectly_analyzed.__len__() / test_data.__len__()) * 100.00)

both_constants = [0.83]
first_constants = [0.91]
last_constants = [0.93]

f = open("results.txt", "w+")
xyz=0
buffer = []
for x in both_constants:
    for y in first_constants:
        for z in last_constants:
            buffer.append((Evaluate(x, y, z), (str(x) + " " + str(y) + " " + str(z))))

for x in sorted(buffer):
    f.write(str(x) + " " + str(y) + " " + str(z) + " --> " + str(x.__getitem__(0)) + "\n")
#Evaluate(0.85, 0.9, 0.95)