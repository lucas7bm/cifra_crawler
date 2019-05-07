import time
import traceback
import pickle

from test_database import TEST_DATABASE, TDB
from cifra import Cifra

def dump_database():
    start_time = time.time()

    test_data = []
    for x in TEST_DATABASE:
        print(':', end='')
        if (x.__getitem__(0) != ""):
            try:
                cifra = Cifra(x.__getitem__(0))
                test_data.append((cifra, x.__getitem__(1)))
            except:
                print("Cifra com problemas: ", x.__getitem__(0))
                traceback.print_exc()

    file_pi = open("cifras.pickle", 'wb')
    pickle.dump(test_data, file_pi)
    file_pi.close()
    print("\nData dump: " + str(len(test_data)) +  " songs in " + str((time.time() - start_time)) + " seconds")


def evaluate(BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT):
    start_time = time.time()
    filehandler = open('cifras.pickle', 'rb')
    test_data = pickle.load(filehandler)
    print("Length: ", len(test_data))
    # now lets tezt dis boi
    incorrectly_analyzed = []
    probl_chords = []
    for x in test_data:
        print('.', end='')
        for chord in x.__getitem__(0).problematic_chords:
            probl_chords.append(chord)

        if (x.__getitem__(0).estimate_tonality(BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT) != x.__getitem__(1)):
            incorrectly_analyzed.append(x)
            #print(x.__getitem__(0).url, " --> Found: ", x.__getitem__(0).found_tone, ". Given: ", x.__getitem__(0).given_tone, ". Tone: ", x.__getitem__(1))
            #print(x.__getitem__(0).fields_distances)

    probl_chords = set(probl_chords)
    #print("\n\n>20: ", more_than_twenty.__len__())
    #print("13-20: ", thirteen_to_twenty.__len__())
    #print("8-12: ", eight_to_twelve.__len__())
    #print("<7: ", less_than_seven.__len__())

    print("\n\n", BOTH_CONSTANT, " ", FIRST_CONSTANT, " ", LAST_CONSTANT)
    print("Success rate: ", 100.00 - ((incorrectly_analyzed.__len__() / test_data.__len__()) * 100.00))
    print("Evaluation: %s seconds" % (time.time() - start_time))
    #print("\n", probl_chords)
    return 100.00 - ((incorrectly_analyzed.__len__() / test_data.__len__()) * 100.00)

#dump_database()

start_time = time.time()

both_constants = [0.9, 0.88, 0.86, 0.84, 0.82, 0.80]
first_constants = [0.93, 0.91, 0.89, 0.87, 0.85]
last_constants = [0.95, 0.93, 0.91, 0.89]

f = open("results.txt", "w+")
buffer = []
for x in both_constants:
    for y in first_constants:
        for z in last_constants:
            buffer.append((evaluate(x, y, z), (str(x) + " " + str(y) + " " + str(z))))

for x in sorted(buffer):
    f.write(str(x.__getitem__(1)) + " --> " + str(x.__getitem__(0)) + "\n")

print("Whole set of evaluations: %s seconds" % (time.time() - start_time))
