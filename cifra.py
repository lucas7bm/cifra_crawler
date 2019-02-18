from bs4 import BeautifulSoup
import requests


class Cifra:
    """ Classe que representa uma cifra musical

    :param str url: A URL de origem da cifra



    """

    # Esta classe representa uma cifra musical com o intuito de ser processada depois.
    # ATRIBUTOS
    #   artist, song, genre: Informações básicas da música
    #            given_tone: A tonalidade central da música (informada pelo escritor da mesma)
    #           chord_array: Uma string contendo a sequência completa de acordes da música
    #        present_chords: Uma string contendo a lista de acordes existentes na cifra (sem repetição)
    #

    def __init__(self, url):
        self.url = url
        song_page = requests.get(url)
        soup_song = BeautifulSoup(song_page.text, 'lxml')

        # Atributos básicos
        self.artist = soup_song.find('h2').text
        self.song = soup_song.find('h1', class_="t1").text
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


#        print(self.song + ", uma música de " + self.artist + ", do gênero " + self.genre + ". O tom desta música é " + self.given_tone + ".")
#        print("Esta música tem um total de", len(self.present_chords), "acordes, fazendo", len(self.chord_array), "usos de acorde.")
#        print(self.present_chords)
#        print()
