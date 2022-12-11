import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt

# Remi Goldfarb
# Genius API

API_KEY = "HAQwWUcRzMqn3cp-AkOLU0WbsB9bqn4tJ56O_kg8ykbLyYMFoqDgUJ6oxt0MBsuY"
#REDIRECT_URI = "http://localhost"

from lyricsgenius import Genius
genius = Genius(API_KEY)

list_1 = []
list_2 = []
list_3 = []
list_4 = []

def song_functions():
  artist = genius.search_artist("SZA", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  list_1.append(artist.songs)
  artist.save_lyrics()
  artist = genius.search_artist("A Boogie wit da Hoodie", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  list_2.append(artist.songs)
  artist.save_lyrics()
  artist = genius.search_artist("Lana Del Rey", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  list_3.append(artist.songs)
  artist.save_lyrics()
  artist = genius.search_artist("Taylor Swift", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  list_4.append(artist.songs)
  artist.save_lyrics()
  #return artist.songs
    
  
#artist = genius.search_artist("Drake", max_songs = 100, sort = 'popularity')
#print(artist.songs)

# create table
def create_tables(cur, conn):
  cur.execute('DROP TABLE IF EXISTS SongsAudiodb')
  cur.execute("CREATE TABLE IF NOT EXISTS SongsAudiodb ((full_title TEXT PRIMARY KEY, name TEXT, year INT)")
  conn.commit()


  
# insert data into table 
def add_data(cur, conn):
  print(list_1)
  for item in range(len(full_title)):
    title_column = full_title[item]
    name_column = name[item]
    year_column = year[item]
    cur.execute("INSERT OR IGNORE INTO SongsAudiodb (full_title, name, year) VALUES (?, ?, ?)", (title_column, name_column, year_column))
    conn.commit()


  #if i decide to put parameters in just update both song_functions()
  #find one of the sql functions that inserts info into the database
  
#find average length of the title and compare it to popularity

song_functions()
add_data(cur, conn)