# -*- coding: utf-8 -*-
#coding: utf-8

from pychord2 import Chord
import requests
from bs4 import BeautifulSoup
from cifra import Cifra

artist_url = "https://www.cifraclub.com.br/chico-buarque/"
artist_page = requests.get(artist_url)

soupArtist = BeautifulSoup(artist_page.text, 'lxml')

soup_songs_list = soupArtist.find(class_="list-links art_musics alf all")
soup_songs_links = soup_songs_list.find_all("a", class_="art_music-link")

links = []
for link in soup_songs_links:
    links.append(link.get('href'))

problematic_chords = set()
problematic_songs = []

total_chords = 0
parsed_chords = 0
for link in links:
    legivel = True
    try:
        cifra = Cifra("https://www.cifraclub.com.br" + link)
        for chord in cifra.present_chords:
            total_chords += 1
            try:
                ch = Chord(chord)
                print(chord, ": ", ch.components())
                parsed_chords += 1
            except:
                print("I see a ", chord, "chord on the song", link, ", but I can't read it! :(")
                legivel = False
                problematic_chords.append(chord)
                problematic_songs.append(link)
    except:
        print("There are no chords here, pal.")
    if (not legivel):
        problematic_songs.append(link)


print("Total de acordes: ", total_chords)
print("Acordes legíveis: ", parsed_chords)
print("Taxa de aproveitamento: ", (parsed_chords/total_chords)*100, "%")
print("Problematic: ", problematic_songs)
print("Problematic Songs rate: ", len(problematic_songs)/len(links), "%")
