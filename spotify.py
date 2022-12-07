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


# Set up the database given the db_name
def set_up_db(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def make_visualizations(cur,conn):
    pass

def main():
    cur, conn = set_up_db('music.db')
    make_visualizations(cur,conn)

if __name__ == "__main__":
    main()