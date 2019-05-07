from pychord import Chord
from pychord.constants.scales import HARMONIC_FIELDS
from tonal_pitch_space import TonalPitchSpace
from bs4 import BeautifulSoup
from test_database import TEST_DATABASE, TDB
import requests, time, traceback
import matplotlib.pyplot as plt

class Cifra:
    """ Classe que representa uma cifra musical
    :param str url: A URL de origem da cifra
    :param double FIRST_CHORD_CONSTANT
    :param double LAST_CHORD_CONSTANT
    :param double BOTH_CHORDS_CONSTANT
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

        self.fields_distances = []

    def harmonic_field_distance(self, field, BOTH_CHORDS_CONSTANT, FIRST_CHORD_CONSTANT, LAST_CHORD_CONSTANT):
        tonal_pitch_space = TonalPitchSpace(field)
        distance = 0
        for chord in self.parsed_chords:
            distance += tonal_pitch_space.distance(chord)


        if (self.parsed_chords[0].triad(False) == self.parsed_chords[-1].triad(False) == field.triad(False)):
            distance *= BOTH_CHORDS_CONSTANT
        else:
            if (self.parsed_chords[0].triad(False) == field.triad(False)):
                distance *= FIRST_CHORD_CONSTANT
            if (self.parsed_chords[-1].triad(False) == field.triad(False)):
                distance *= LAST_CHORD_CONSTANT
        return distance

    def estimate_tonality(self, BOTH_CHORDS_CONSTANT, FIRST_CHORD_CONSTANT, LAST_CHORD_CONSTANT):
        fields_distances = []
        for field in HARMONIC_FIELDS:
            fields_distances.append([self.harmonic_field_distance(Chord(field), BOTH_CHORDS_CONSTANT, FIRST_CHORD_CONSTANT, LAST_CHORD_CONSTANT), field])
        self.fields_distances = sorted(fields_distances)
        self.found_tone = self.fields_distances[0].__getitem__(1)
        return self.found_tone