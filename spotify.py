import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Caleigh Crossman
# Spotify API 

url = "https://api.spotify.com/v1/search?query=year%3A2022&type=track&market=US&offset=0&limit=2"
song_ids = []
valence_lst = []
energy_lst = []
danceability_lst = []

# Make request and return data dictionary
def make_request(playlist_id):
    client_secret = "347d645c39984caf80481f28342735aa"
    client_id = "2e595246fa1d4684aec2c33575c0271f"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlist = spotify.playlist_tracks(playlist_id,fields='items(track(name,id,popularity,artists))',limit=25)
    for song in playlist['items']:
        id = song['track']['id']
        song_info = spotify.audio_features(id)
        valence_lst.append(song_info[0]['valence'])
        danceability_lst.append(song_info[0]['danceability'])
        energy_lst.append(song_info[0]['energy'])
    return playlist

# Create table with list of genre IDs and genres
def create_artists_table(cur,conn):
    cur.execute("DROP TABLE IF EXISTS Artists")
    cur.execute("CREATE TABLE Artists (artist_id TEXT PRIMARY KEY, artist TEXT)")
    conn.commit()
    

# Create the table called songs
def make_songs_table(cur,conn):
    cur.execute("DROP TABLE IF EXISTS Songs")
    cur.execute("CREATE TABLE Songs (song_name TEXT PRIMARY KEY, song_id TEXT, artist_id TEXT, popularity INTEGER, \
                valence FLOAT, danceability FLOAT, energy FLOAT)")
    conn.commit()
    
# Add 25 songs at a time to table
def add_songs(data,cur,conn):
    i = 0
    for track in data['items']:
        song_name = track['track']['name']
        song_id = track['track']['id']
        popularity = track['track']['popularity']
        valence = valence_lst[i]
        danceability = danceability_lst[i]
        energy = energy_lst[i]
        i+=1
        cur.execute('SELECT artist_id FROM Artists WHERE artist = ?',(track['track']['artists'][0]['name'], ))
        artist_id = cur.fetchone()[0]
        cur.execute("INSERT OR IGNORE INTO Songs (song_name,song_id,artist_id,popularity,valence,danceability,energy) VALUES (?,?,?,?,?,?,?)",(song_name,song_id,artist_id,popularity,valence,danceability,energy))
    conn.commit()

# Reads and loads the json data from the file
def read_data(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data

# Write the json data to a file 
def write_json(filename,dict):
    jsonString = json.dumps(dict)
    with open(filename, 'w') as outFile:
        outFile.write(jsonString)

def make_visualizations(cur,conn):
    pass

