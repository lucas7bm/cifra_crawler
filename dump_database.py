import traceback, time, pickle
from test_database import TEST_DATABASE
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

dump_database()