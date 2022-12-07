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

# Set up the database given the db_name
def set_up_db(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Create table with list of genre IDs and genres
def create_artists_table(cur,conn):
    cur.execute("DROP TABLE IF EXISTS Artists")
    cur.execute("CREATE TABLE Artists (artist_id TEXT PRIMARY KEY, artist TEXT)")
    conn.commit()


def make_visualizations(cur,conn):
    pass

def main():
    make_request()
    cur, conn = set_up_db('music.db')
    make_visualizations(cur,conn)

if __name__ == "__main__":
    main()