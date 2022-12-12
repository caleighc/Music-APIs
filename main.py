import unittest
import sqlite3
import json
import os

# import all our files
import spotify
import genius
import audio

# Set up the database given the db_name
def set_up_db(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def run_spotify(cur,conn):
    # Create tables for spotify 
    spotify.create_artists_table(cur,conn)
    spotify.create_songs_table(cur,conn)
    # Add data to both tables
    playlist_ids = ["37i9dQZF1DX7Jl5KP2eZaS","37i9dQZF1DX0kbJZpiYdZl","6SjN06zZBZpsCWJk2DwhDs","3KHb0WRmzbp9WH7E2mXVmx","0chdKQr18NN9WRI355V8BN"]
    for id in playlist_ids:
        jsonDict = spotify.make_request(id)
        spotify.add_artists_id(jsonDict,cur,conn)
        spotify.add_songs(jsonDict,cur,conn)
    # Make calculations and visualizations for spotify 
    #spotify.make_visualizations(cur,conn)
    #spotify.artists_visualization(cur,conn)

def run_audio(cur,conn):
    artist_id = ['20244d07-534f-4eff-b4d4-930878889970', '9fff2f8a-21e6-47de-a2b8-7f449929d43f', '381086ea-f511-4aba-bdf9-71c753dc5077', '65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab', 'c8b03190-306c-4120-bb0b-6f2ebfc06ea9',
    'e0140a67-e4d1-4f13-8a01-364355bee46e', 'f4fdbb4c-e4b7-47a0-b83b-d91bbfcfa387', 'f27ec8db-af05-4f36-916e-3d57f91ecf5e', '73e5e69d-3554-40d8-8516-00cb38737a1c', 'b8a7c51f-362c-4dcb-a259-bc6e0095f0a6']
    for id in artist_id:
        audio.request_data(id)
    # Create tables for audio-db 
    audio.create_table(cur, conn)
    # Add data for audio-db
    audio.insert_data(cur, conn)
    audio.calculate(cur, conn)
    
def run_genius(cur,conn):
    # Create tables for genius
    genius.song_functions()
    genius.create_tables(cur,conn)
    # Add data for genius 
    genius.add_data(cur, conn)

def main(): 
    cur,conn = set_up_db("music.db") 
    # run spotify
    run_spotify(cur,conn)
    # run audio
    run_audio(cur,conn)
    # run genius
    run_genius(cur,conn)


if __name__ == "__main__":
    main()
