import time
import pickle
from tonal_pitch_space import TonalPitchSpace
from pychord import Chord

def evaluate_group(test_data, BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT):
    probl_chords = []
    incorrectly_analyzed = []

    for x in test_data:
        print('.', end='')
        for chord in x.__getitem__(0).problematic_chords:
            probl_chords.append(chord)

        if (x.__getitem__(0).estimate_tonality(BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT) != x.__getitem__(1)):
            incorrectly_analyzed.append(x)

    #probl_chords = set(probl_chords)
    #print("\n", probl_chords)

    print(len(incorrectly_analyzed), " mistakes on a group of ", test_data.__len__(), " songs.")
    # for x in incorrectly_analyzed:
    #    print(x.__getitem__(0).url, " Given: ", x.__getitem__(0).given_tone, " - Found: ", x.__getitem__(0).found_tone, " - Correct: ", x.__getitem__(1))
    #    print(x.__getitem__(0).fields_distances)
    print("Success rate on group: ", '{:.3f}%'.format(100.00 - ((incorrectly_analyzed.__len__() / test_data.__len__()) * 100.00)))
    return 100.00 - ((incorrectly_analyzed.__len__() / test_data.__len__()) * 100.00)



def evaluate(BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT):
    start_time = time.time()
    filehandler = open('cifras.pickle', 'rb')
    test_data =  pickle.load(filehandler)
    print("GENERAL INFO")
    print("Length of database: ", len(test_data))
    print("Parameters: ", BOTH_CONSTANT, " ", FIRST_CONSTANT, " ", LAST_CONSTANT)
    # now lets tezt dis boi

    #If evaluating considering complexity categories
    more_than_twenty = []
    fifteen_to_twenty = []
    nine_to_fourteen = []
    five_to_eight = []
    up_to_four = []

    for x in test_data:
        if x.__getitem__(0).present_chords.__len__() > 20:
            more_than_twenty.append(x)
        if x.__getitem__(0).present_chords.__len__() > 14:
            fifteen_to_twenty.append(x)
        elif x.__getitem__(0).present_chords.__len__() > 8:
            nine_to_fourteen.append(x)
        elif x.__getitem__(0).present_chords.__len__() > 5:
            five_to_eight.append(x)
        else:
            up_to_four.append(x)

    print("\n    >20: ", more_than_twenty.__len__())
    print(  "  15-20: ", fifteen_to_twenty.__len__())
    print(  "   9-14: ", nine_to_fourteen.__len__())
    print(  "    5-8: ", five_to_eight.__len__())
    print(  "     <5: ", up_to_four.__len__(), "\n")

    print("EVALUATION OF EACH COMPLEXITY CATEGORY")
    average = 0
    print("  >20  evaluation")
    average += evaluate_group(more_than_twenty, BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT)


    print("\n15-20  evaluation")
    average += evaluate_group(fifteen_to_twenty, BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT)


    print("\n 9-14  evaluation")
    average += evaluate_group(nine_to_fourteen, BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT)


    print("\n   5-8  evaluation")
    average += evaluate_group(five_to_eight, BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT)

    print("\n   <5  evaluation")
    average += evaluate_group(up_to_four, BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT)

    print("\nEVALUATION OF THE WHOLE DATASET")
    eval = evaluate_group(test_data, BOTH_CONSTANT, FIRST_CONSTANT, LAST_CONSTANT)
    print("Sucess rate: ", eval)

    average /= 5
    print("Success rate (average): ", average)

    print("\nEvaluation done in %s seconds" % (time.time() - start_time) + "\n\nEND OF EVALUATION\n\n")

    number_of_chords = [0] * 40
    for x in test_data:
        number_of_chords[x.__getitem__(0).present_chords.__len__() - 1] += 1

    print(number_of_chords)

    return average

start_time = time.time()

both_constants = [0.82]
first_constants = [0.91]
last_constants = [0.92]

f = open("results.txt", "w+")
buffer = []
for x in both_constants:
    for y in first_constants:
        for z in last_constants:
            buffer.append((evaluate(x, y, z), (str(x) + " " + str(y) + " " + str(z))))

for x in sorted(buffer):
    f.write(str(x.__getitem__(1)) + " --> " + str(x.__getitem__(0)) + "\n")

print("\n\nWhole set of evaluations: %s seconds" % (time.time() - start_time))