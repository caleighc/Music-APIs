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
  list_1 = artist.songs
  artist.save_lyrics()
  artist = genius.search_artist("A Boogie wit da Hoodie", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  list_2 = artist.songs
  artist.save_lyrics()
  artist = genius.search_artist("Lana Del Rey", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  list_3 = artist.songs
  artist.save_lyrics()
  artist = genius.search_artist("Taylor Swift", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  list_4 = artist.songs
  artist.save_lyrics()
  return list_1, list_2, list_3, list_4
    
  
#artist = genius.search_artist("Drake", max_songs = 100, sort = 'popularity')
#print(artist.songs)

# create table
def make_tables(cur, conn):
  cur.execute('DROP TABLE IF EXISTS Genius')
  cur.execute("CREATE TABLE IF NOT EXISTS Genius (full_title TEXT PRIMARY KEY, name TEXT, year INT)")
  conn.commit()

#f = open ('Lyrics_SZA.json', "r")
#data  = json.loads(f.read())
#for i in data:
  #print(i)
def add_data(cur, conn): 
  with open("Lyrics_SZA.json", "r") as f:
    data = json.load(f)
    title_column = data["songs"][0]["full_title"]
    print(title_column)
    name_column = data["name"]
    print(name_column)
    year_column = data["songs"][0]["release_date_components"]["year"]
    print(year_column)
    cur.execute("INSERT OR IGNORE INTO SongsAudiodb (title_column, name_column, year_column) VALUES (?, ?, ?)", (title_column, name_column, year_column))
    conn.commit()

  #print(list_1)
  #for item in range(len("full_title")):
    #title_column = data["songs"]["full_title"][item]
    #name_column = data["name"][item]
    #year_column = data["songs"]["year"][item]
    #cur.execute("INSERT OR IGNORE INTO SongsAudiodb (Lyrics_SZA.json[full_title], Lyrics_SZA.json[name], Lyrics_SZA.json[year]) VALUES (?, ?, ?)", (title_column, name_column, year_column))
    #conn.commit()
#f.close()


  #if i decide to put parameters in just update both song_functions()
  #find one of the sql functions that inserts info into the database
  
#find average length of the title and compare it to popularity

