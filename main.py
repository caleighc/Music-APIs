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
    jsonDict = spotify.make_request()
    spotify.add_artists_id(jsonDict,cur,conn)
    spotify.add_songs(jsonDict,cur,conn)
    spotify.make_visualizations(cur,conn)
    spotify.artists_visualization(cur,conn)

def run_audio(cur,conn):
    artist_id = ['20244d07-534f-4eff-b4d4-930878889970', '9fff2f8a-21e6-47de-a2b8-7f449929d43f', '381086ea-f511-4aba-bdf9-71c753dc5077', '65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab', 'c8b03190-306c-4120-bb0b-6f2ebfc06ea9',
    'e0140a67-e4d1-4f13-8a01-364355bee46e', 'f4fdbb4c-e4b7-47a0-b83b-d91bbfcfa387', 'f27ec8db-af05-4f36-916e-3d57f91ecf5e', '73e5e69d-3554-40d8-8516-00cb38737a1c', 'b8a7c51f-362c-4dcb-a259-bc6e0095f0a6']
    for id in artist_id:
        audio.request_data(id)

    # Create tables for audio-db 
    audio.create_table(cur, conn)

    # Add data for audio-db
    audio.insert_data(cur, conn) 

    # calculations/visualizations
    result1 = audio.calculate1(cur, conn)
    audio.write_to_csv1(result1)
    audio.make_chart1(result1)

    result2 = audio.calculate2(cur, conn)
    audio.write_to_csv2(result2)
    audio.make_chart2()

def run_genius(cur,conn):
    # Create tables for genius
    genius.song_functions()
    genius.new_tables(cur,conn)
    # Add data from genius 
    genius.add_data_1(cur, conn)
    genius.add_data_2(cur, conn)
    genius.add_data_3(cur, conn)
    genius.add_data_4(cur, conn)
    #genius._get(path, params=None, headers=None)
    #genius.get_artist_songs(artist_id)
    #genius.get_song_information(song_ids)
    #genius.writing_json_genius(files,dict)
    genius.make_visualizations_hist(cur, conn)

def main(): 
    cur,conn = set_up_db("music.db") 
    run_spotify(cur,conn)
    #run_audio(cur,conn)
    #run_genius(cur,conn)


if __name__ == "__main__":
    main()
