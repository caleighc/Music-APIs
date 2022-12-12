import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import numpy as np
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
    # Get the tracks on the playlist 
    playlist = spotify.playlist_tracks(playlist_id,fields='items(track(name,id,popularity,artists))',limit=25)
    # Get the song_id for each track and then make another request to get data on each song
    for song in playlist['items']:
        id = song['track']['id']
        song_info = spotify.audio_features(id)
        valence_lst.append(song_info[0]['valence'])
        danceability_lst.append(song_info[0]['danceability'])
        energy_lst.append(song_info[0]['energy'])
    return playlist

# Create table with list of artist IDs and artists
def create_artists_table(cur,conn):
    cur.execute("CREATE TABLE Artists (artist_id TEXT PRIMARY KEY, artist TEXT)")
    conn.commit()
    
# Create the table called songs which contains information about each song
def create_songs_table(cur,conn):
    cur.execute("CREATE TABLE Songs (song_name TEXT PRIMARY KEY, song_id TEXT, artist_id TEXT, popularity INTEGER, \
                valence FLOAT, danceability FLOAT, energy FLOAT)")
    conn.commit()
    
# Adds artist ids
def add_artists_id(data,cur,conn):
    artist_lst = []
    for track in data['items']:
        artist = track['track']['artists'][0]['name']
        id = track['track']['artists'][0]['id']
        cur.execute("INSERT OR IGNORE INTO Artists (artist_id,artist) VALUES (?,?)",(id,artist))
    conn.commit()
    
# Add 25 songs at a time to table
def add_songs(data,cur,conn):
    for i, track in enumerate(data['items']):
        song_name = track['track']['name']
        song_id = track['track']['id']
        popularity = track['track']['popularity']
        valence = valence_lst[i]
        danceability = danceability_lst[i]
        energy = energy_lst[i]
        cur.execute('SELECT artist_id FROM Artists WHERE artist = ?',(track['track']['artists'][0]['name'], ))
        artist_id = cur.fetchone()[0]
        cur.execute("INSERT OR IGNORE INTO Songs (song_name,song_id,artist_id,popularity,valence,danceability,energy) VALUES (?,?,?,?,?,?,?)",(song_name,song_id,artist_id,popularity,valence,danceability,energy))
    conn.commit()

# Calculate line of best fit and make visualizations 
def make_visualizations(cur,conn):
    plt.figure()
    cur.execute(
    """
    SELECT danceability,energy
    FROM Songs
    """
    )
    res = cur.fetchall()
    conn.commit()
    x,y = list(map(list, zip(*res)))
    x = np.array(x)
    y = np.array(y)
    # Calculate the slope
    n = len(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    sxy = np.sum(x*y) - n*mean_x*mean_y
    sxx = np.sum(x*x) - n*mean_x*mean_x
    slope = sxy/sxx
    b = mean_y-slope*mean_x
    line_best_fit = slope * x + b
    print(f"The slope is {slope}")
    print(f"The y-intercept is {b}")
    print(f"The line of best fit is y = {slope}*x + {b}")
    # Plot the scatter and line of best fit
    plt.xlabel('Danceability')
    plt.ylabel('Energy')
    plt.title("Danceability vs. Energy")
    plt.scatter(x,y,color='blue')
    plt.plot(x,line_best_fit, color='red')
    plt.show()
    # Calculation coefficient of determination
    error = y - line_best_fit
    standard_error = np.sum(error**2)
    mse = standard_error/n
    rmse = np.sqrt(mse)
    sst = np.sum((y-mean_y)**2)
    r_squared = 1 - (standard_error/sst)
    print(f"The coefficient of determination (R^2) is {r_squared}")
    f = open("output.txt", 'w')
    f.write(f"The slope is {slope}")
    f.write(f"The y-intercept is {b}")
    f.write(f"The line of best fit is y = {slope}*x + {b}")
    f.close()
    
# Create visualization of artists 
def artists_visualization(cur,conn):
    plt.figure()
    cur.execute(
    """
    SELECT artists.artist, COUNT(*)
    FROM songs 
    JOIN Artists ON artists.artist_id = Songs.artist_id
    GROUP BY artist
    HAVING COUNT(*) > 1
    """
    )
    result = cur.fetchall()
    conn.commit()
    types = {}
    for item in result:
        types[item[0]] = item[1]
    y = list(types.keys())
    x = list(types.values())
    plt.title("Artists that have > 1 song on top charts")
    plt.ylabel('Artists')
    plt.xlabel('Number of songs')
    plt.barh(y,x)
    plt.show()



