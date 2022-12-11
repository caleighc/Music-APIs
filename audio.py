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
artist_id = []
artist = []
# genre = []
score = []
votes = []

# make request
def request_data(artist_ids):

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


    url = 'http://theaudiodb.com/api/v1/json/523532/track-top10-mb.php?s=' + artist_ids
    response = requests.get(url)

    data = response.text

    # get song id
    regex = r'"idTrack":"([0-9]{8})"'
    temp = re.findall(regex, data)
    for item in temp:
        song_id.append(int(item))

    # get song name 
    regex = r'"strTrack":"([\w+\s*\(*\)*\**\.*\&*\'*\,*\-*\?*\!*]{1,})"'
    temp = re.findall(regex, data)
    for item in temp:
        song.append(item)

    # get artist id
    regex = r'"idArtist":"([0-9]{6})"'
    temp = re.findall(regex, data)
    for item in temp:
        item = int(item)
        artist_id.append(item)

    # get artist name
    regex = r'"strArtist":"([\w+\s*]{1,})"'
    temp = re.findall(regex, data)
    for item in temp:
        artist.append(item)

    

    # get song score 
    regex = r'"intScore":"{0,1}([0-9*.*0-9*]{1,}|null)"{0,1}'
    temp = re.findall(regex, data)
    for item in temp:
        score.append(item)

    # get num votes 
    regex = r'"intScoreVotes":"{0,1}([0-9]{1,}|null)"{0,1}'
    temp = re.findall(regex, data)
    for item in temp:
        votes.append(item)



    # # get song genre 
    # regex = r'"strGenre":"([\w+\s*\/*\-*\&*]{1,})"'
    # temp = re.findall(regex, data)
    # for item in temp:
    #     genre.append(item)



# create table
def create_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS SongsAudiodb')
    cur.execute("CREATE TABLE IF NOT EXISTS SongsAudiodb (song_id INT PRIMARY KEY, song TEXT, artist_id INT, score TEXT, votes TEXT)")

    cur.execute('DROP TABLE IF EXISTS ArtistsAudiodb')
    cur.execute("CREATE TABLE IF NOT EXISTS ArtistsAudiodb (artist_id INT PRIMARY KEY, artist TEXT)")

    conn.commit()


# insert data into table 
def insert_data(cur, conn):
    # songs table
    for item in range(0, 25):
        id_temp = song_id[item]
        song_temp = song[item]
        artist_id_temp = artist_id[item]
        if score[item] != 'null':
            score_temp = float(score[item])
        else:
            score_temp = None
            
        if votes[item] != 'null':
            votes_temp = int(votes[item])
        else:
            votes_temp = None
        cur.execute("INSERT OR IGNORE INTO SongsAudiodb (song_id, song, artist_id, score, votes) VALUES (?, ?, ?, ?, ?)", (id_temp, song_temp, artist_id_temp, score_temp, votes_temp))
    for item in range(25, 50):
        id_temp = song_id[item]
        song_temp = song[item]
        artist_id_temp = artist_id[item]
        if score[item] != 'null':
            score_temp = float(score[item])
        else:
            score_temp = None
            
        if votes[item] != 'null':
            votes_temp = int(votes[item])
        else:
            votes_temp = None
        cur.execute("INSERT OR IGNORE INTO SongsAudiodb (song_id, song, artist_id, score, votes) VALUES (?, ?, ?, ?, ?)", (id_temp, song_temp, artist_id_temp, score_temp, votes_temp))
    for item in range(50, 75):
        id_temp = song_id[item]
        song_temp = song[item]
        artist_id_temp = artist_id[item]
        if score[item] != 'null':
            score_temp = float(score[item])
        else:
            score_temp = None
            
        if votes[item] != 'null':
            votes_temp = int(votes[item])
        else:
            votes_temp = None
        cur.execute("INSERT OR IGNORE INTO SongsAudiodb (song_id, song, artist_id, score, votes) VALUES (?, ?, ?, ?, ?)", (id_temp, song_temp, artist_id_temp, score_temp, votes_temp))
    for item in range(75, 100):
        id_temp = song_id[item]
        song_temp = song[item]
        artist_id_temp = artist_id[item]
        if score[item] != 'null':
            score_temp = float(score[item])
        else:
            score_temp = None
            
        if votes[item] != 'null':
            votes_temp = int(votes[item])
        else:
            votes_temp = None
        cur.execute("INSERT OR IGNORE INTO SongsAudiodb (song_id, song, artist_id, score, votes) VALUES (?, ?, ?, ?, ?)", (id_temp, song_temp, artist_id_temp, score_temp, votes_temp))

    # artist table
    for item in range(0, len(artist_id), 10):
        id_temp = artist_id[item]
        artist_temp = artist[item]
        cur.execute("INSERT OR IGNORE INTO ArtistsAudiodb (artist_id, artist) VALUES (?, ?)", (id_temp, artist_temp))

    conn.commit()

def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

# calculate the average score for each artist 
def calculate(cur, conn):
    # cur.execute("SELECT a.artist, avg(s.votes) from SongsAudiodb s join ArtistsAudiodb a on s.artist_id = a.artist_id group by a.artist")
    # result = cur.fetchall()
    # conn.commit()
    # print(result)

    cur.execute("SELECT a.artist, avg(s.score) from SongsAudiodb s join ArtistsAudiodb a on s.artist_id = a.artist_id group by a.artist")
    result = cur.fetchall()
    conn.commit()

    x = []
    y = []
    for i in result:
        x.append(i[0])
        y.append(round(i[1], 2))
    plt.bar(x, y)
    addlabels(x, y)
    plt.title("Average Score of Artists' Top 10 Songs")
    plt.xlabel("Artist")
    plt.ylabel("Average Score")
    plt.show()



def main():

    artist_ids = ['20244d07-534f-4eff-b4d4-930878889970', '9fff2f8a-21e6-47de-a2b8-7f449929d43f', '381086ea-f511-4aba-bdf9-71c753dc5077', '65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab', 'c8b03190-306c-4120-bb0b-6f2ebfc06ea9',
    'e0140a67-e4d1-4f13-8a01-364355bee46e', 'f4fdbb4c-e4b7-47a0-b83b-d91bbfcfa387', 'f27ec8db-af05-4f36-916e-3d57f91ecf5e', '73e5e69d-3554-40d8-8516-00cb38737a1c', 'b8a7c51f-362c-4dcb-a259-bc6e0095f0a6']
    for id in artist_ids:
        request_data(id)



if __name__ == "__main__":
    main()
