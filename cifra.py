from pychord import Chord
from pychord.constants.scales import HARMONIC_FIELDS
from tonal_pitch_space import TonalPitchSpace
from bs4 import BeautifulSoup
from test_database import TEST_DATABASE, TDB
import requests, time
import matplotlib.pyplot as plt

class Cifra:
    """ Classe que representa uma cifra musical
    :param str url: A URL de origem da cifra
    """

    # Esta classe representa uma cifra musical com o intuito de ser processada depois.
    # ATRIBUTOS
    #   artist, title, genre: Informações básicas da música
    #            given_tone: A tonalidade central da música (informada pelo escritor da mesma)
    #           chord_array: Uma string contendo a lista completa de acordes da música
    #        present_chords: Uma string contendo o conjunto de acordes existentes na cifra (sem repetição)
    #         parsed_chords: Lista de todos os acordes que foram devidamente
    #                        identificados e processados através do pychord
    #          fully_parsed: Um boolean que indica se todos os acordes foram interpretados
    #      fields_distances: O resultado do cálculo de distância utilizando todos os 24 campos harmônicos.
    #                        É ordenado da menor distância (tonalidade mais provável) para a maior.
    #            found_tone: A tonalidade encontrada,

    def __init__(self, url):
        self.url = url
        song_page = requests.get(url)
        soup_song = BeautifulSoup(song_page.text, 'lxml')

        # Atributos básicos
        self.artist = soup_song.find('h2').text
        self.title = soup_song.find('h1', class_="t1").text
        self.given_tone = soup_song.find(id="cifra_tom").a.text

        # Às vezes, quando um artista não possui gênero musical informado, o site exibe a letra inicial de seu nome
        # Este 'if' a seguir busca evitar que esta letra seja utilizada como gênero
        self.genre = "Unknown Genre"
        if len(soup_song.find(itemprop="title").text) > 1: self.genre = soup_song.find(itemprop="title").text

        self.chord_array = []
        soup_chords = soup_song.find("pre").find_all('b')
        for soupChord in soup_chords:
            self.chord_array.append(soupChord.text)
        self.present_chords = set(self.chord_array)

        self.parsed_chords = []
        self.problematic_chords = []
        for chord in self.chord_array:
            try:
                chord = Chord(chord)
                self.parsed_chords.append(chord)
            except:
                self.problematic_chords.append(chord)

        self.problematic_chords = set(self.problematic_chords)

        self.fully_parsed = False
        if (self.problematic_chords.__len__() == 0):
            self.fully_parsed = True

        self.fields_distances = [()]
        self.estimate_tonality()
        self.found_tone = self.fields_distances[0].__getitem__(1)


    def harmonic_field_distance(self, field):
        tonal_pitch_space = TonalPitchSpace(field)
        distance = 0
        for chord in self.parsed_chords:
            distance += tonal_pitch_space.distance(chord)
        return distance

    def estimate_tonality(self):
        fields_distances = []
        for field in HARMONIC_FIELDS:
            fields_distances.append([self.harmonic_field_distance(Chord(field)), field])
        self.fields_distances = sorted(fields_distances)

i=0
for x in TEST_DATABASE:
    if(x.__getitem__(0) != ""):
        i += 1
        print(i, ": ", x.__getitem__(0))


less_than_seven = []
seven_to_twelve = []
twelve_to_twenty = []
more_than_twenty = []

start_time = time.time()

test_data = []
record_of_chords = 0

for x in TEST_DATABASE:
    if(x.__getitem__(0) != ""):
        cifra = Cifra(x.__getitem__(0))
        test_data.append(cifra)
        if cifra.present_chords.__len__() > record_of_chords:
            most_complex_song = cifra
            record_of_chords = cifra.present_chords.__len__()

        #Criando as categorias de complexidade
        if cifra.present_chords.__len__() > 20:
            more_than_twenty.append(cifra.url)
            continue
        if cifra.present_chords.__len__() > 12:
            twelve_to_twenty.append(cifra.url)
            continue
        if cifra.present_chords.__len__() > 7:
            seven_to_twelve.append(cifra.url)
            continue
        else:
            less_than_seven.append(cifra.url)

print("Cifra mais complexa: ", most_complex_song.url, ", com ", record_of_chords, " acordes.")
print(most_complex_song.problematic_chords)

print("\n\n>20: ", more_than_twenty.__len__())
print("13-20: ", twelve_to_twenty.__len__())
print("8-12: ", seven_to_twelve.__len__())
print("<7: ", less_than_seven.__len__())


print("\n\n>20: ", more_than_twenty)
print("13-20: ", twelve_to_twenty)
print("8-12: ", seven_to_twelve)
print("<7: ", less_than_seven)

values = [0] * 50
for x in test_data:
    values[x.present_chords.__len__()] += 1

print(values)

print("--- %s seconds ---" % (time.time() - start_time))
