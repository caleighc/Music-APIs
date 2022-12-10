import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt

# Remi Goldfarb
# Genius API

API_KEY = "HAQwWUcRzMqn3cp-AkOLU0WbsB9bqn4tJ56O_kg8ykbLyYMFoqDgUJ6oxt0MBsuY"
# REDIRECT_URI = "http://localhost"

from lyricsgenius import Genius
genius = Genius(API_KEY)

def song_functions(cur,conn):
    artist = genius.search_artist("Lana Del Ray", max_songs = 100, sort = 'popularity')
    print(artist.songs)
    artist = genius.search_artist("Drake", max_songs = 100, sort = 'popularity')
    print(artist.songs)
    

#artists = []
#while True:
    #try:
        #artists.append(genius.search_artist("Ariana Grande", max_songs=100))
        #artists.append(genius.search_artist("Drake", max_songs=100))
        #break
    #except:
        #pass



def create_tables(cur,conn):
   cur.execute("CREATE TABLE IF NOT EXISTS music_name_table (column_music)") 
   #call whatever function adds data to the database
   song_functions(cur,conn)
   cur.execute("INSERT INTO music_name_table (song,id,artist,popularity) VALUES (?,?,?,?)",(song_name,song_id,artist_id,popularity))
   
   conn.commit()
   #if i decide to put parameters in just update both song_functions()
   #find one of the sql functions that inserts info into the database
    

    # find average length of the title and compare it to popularity

    



