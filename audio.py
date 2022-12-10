import unittest
import sqlite3
import requests
import json
import os
import re
import matplotlib
import matplotlib.pyplot as plt

# Ava Webster
# Apple Music API

APIKEY = '523532'
song_id = []
song = []
genre = []
mood = []
style = []
total_listens = []
score = []

# make request
def request_data(artist_id):

    # top artists:
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=20244d07-534f-4eff-b4d4-930878889970') # taylor swift
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=9fff2f8a-21e6-47de-a2b8-7f449929d43f') # drake
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=381086ea-f511-4aba-bdf9-71c753dc5077') # kendrick lamar
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab') # metallica
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=c8b03190-306c-4120-bb0b-6f2ebfc06ea9') # the weeknd
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=859d0860-d480-4efd-970c-c05d5f1776b8') # beyonce
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=f4fdbb4c-e4b7-47a0-b83b-d91bbfcfa387') # ariana grande
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=f27ec8db-af05-4f36-916e-3d57f91ecf5e') # michael jackson
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=73e5e69d-3554-40d8-8516-00cb38737a1c') # rihanna
    # response = requests.get('http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=b8a7c51f-362c-4dcb-a259-bc6e0095f0a6') # ed sheeran


    url = 'http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=' + artist_id
    response = requests.get(url)

    data = response.text

    # get song id
    regex = r'"idTrack":"([0-9]{8})"'
    temp = re.findall(regex, data)
    for item in temp:
        song_id.append(item)

    # get song name 
    regex = r'"strTrack":"([\w+\s*\(*\)*\**\.*\&*\'*\,*\-*\?*\!*]{1,})"'
    temp = re.findall(regex, data)
    for item in temp:
        song.append(item)

    # get song genre 
    regex = r'"strGenre":"([\w+\s*\/*\-*\&*]{1,})"'
    temp = re.findall(regex, data)
    for item in temp:
        genre.append(item)

    # get song mood
    regex = r'"strMood":"([\w+\s*\/*\-*\&*]{1,})"'
    temp = re.findall(regex, data)
    for item in temp:
        mood.append(item)

    # get total listens
    regex = r'"intTotalListeners":"([0-9]{1,})"'
    temp = re.findall(regex, data)
    for item in temp:
        total_listens.append(item)

    # get score
    regex = r'"intScore":"([\d+.*\d*]{1,})"'
    temp = re.findall(regex, data)
    for item in temp:
        score.append(item)


# create database
def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


# create table
def create_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS Music')
    cur.execute("CREATE TABLE IF NOT EXISTS Music (song_id TEXT PRIMARY KEY, song TEXT, genre TEXT")
    conn.commit()


# insert data into table - hw7 first function
def insert_song_id(cur, conn):
    for item in range(len(song_id)):
        id_temp = song_id[item]
        song_temp = song[item]
        genre_temp = genre[item]
        cur.execute("INSERT OR IGNORE INTO Music (song_id, song, genre) VALUES (?, ?, ?)", (id_temp, song_temp, genre_temp))
    conn.commit()


# get calculations 
# sum up each genre total
#** order each genre on a scale, give number, get average genre number and see where it falls on scale of sorted genres
def calculate_genres():
    genre_count = {}
    for item in genre:
        genre_count[item] = genre_count.get(item, 0) + 1
    print(genre_count)



def main():

    artist_id =  ['20244d07-534f-4eff-b4d4-930878889970', '9fff2f8a-21e6-47de-a2b8-7f449929d43f', '381086ea-f511-4aba-bdf9-71c753dc5077', '65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab', 'c8b03190-306c-4120-bb0b-6f2ebfc06ea9',
    '859d0860-d480-4efd-970c-c05d5f1776b8', 'f4fdbb4c-e4b7-47a0-b83b-d91bbfcfa387', 'f27ec8db-af05-4f36-916e-3d57f91ecf5e', '73e5e69d-3554-40d8-8516-00cb38737a1c', 'b8a7c51f-362c-4dcb-a259-bc6e0095f0a6']
    for id in artist_id:
        request_data(id)


    print(len(total_listens))
    print(len(score))

    # print(len(genre))
    # print(song)
    # print(genre)
    # print(mood)
    # print(len(mood))

    calculate_genres()

    # cur, conn = set_up_db('music.db')
  

if __name__ == "__main__":
    main()
