from pychord import Chord
from pychord.constants.scales import HARMONIC_FIELDS
from tonal_pitch_space import TonalPitchSpace
from bs4 import BeautifulSoup
import requests


class Cifra:
    """ Classe que representa uma cifra musical
    :param str url: A URL de origem da cifra
    """

    # Esta classe representa uma cifra musical com o intuito de ser processada depois.
    # ATRIBUTOS
    #   artist, title, genre: Informações básicas da música
    #            given_tone: A tonalidade central da música (informada pelo escritor da mesma)
    #           chord_array: Uma string contendo a sequência completa de acordes da música
    #        present_chords: Uma string contendo a lista de acordes existentes na cifra (sem repetição)
    #         parsed_chords: Todos os acordes que foram devidamente
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

        self.fully_parsed = False
        if (self.chord_array.__len__() == self.parsed_chords.__len__()):
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

#        print(self.title + ", uma música de " + self.artist + ", do gênero " + self.genre + ". O tom desta música é " + self.given_tone + ".")
#        print("Esta música tem um total de", len(self.present_chords), "acordes, fazendo", len(self.chord_array), "usos de acorde.")
#        print(self.present_chords)
#        print()

cifra = Cifra("https://www.cifraclub.com.br/5-seco/feliz-pra-cachorro/")

#print(cifra.parsed_chords, "\nTamanho do array:", cifra.parsed_chords.__len__())
#print(cifra.problematic_chords)
print("O tom de ", cifra.title, "de ", cifra.artist ," é: ", cifra.found_tone, "\n")
print(cifra.fields_distances, "\n")
print(cifra.chord_array)
print(cifra.fully_parsed)
print(cifra.problematic_chords)