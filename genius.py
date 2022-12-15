import unittest
import sqlite3
import requests, json
import os
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import plotly.express as px
# Remi Goldfarb
# Genius API

BASE_URL = "https://api.genius.com"
CLIENT_ACCESS_TOKEN = "qbk4incT3dzpnkv_Q87iY89o1xjbeMNDxIkTHly-gWGvNNPz56IMlw9Mfgm-7CqH"
ARTIST_NAME = "ABoogiewitdaHoodie"
ARTIST_NAME = "LanaDelRey"
ARTIST_NAME = "SZA"
ARTIST_NAME = "TaylorSwift"
API_KEY = "HAQwWUcRzMqn3cp-AkOLU0WbsB9bqn4tJ56O_kg8ykbLyYMFoqDgUJ6oxt0MBsuY"
#REDIRECT_URI = "http://localhost"

from lyricsgenius import API, PublicAPI, Genius
genius = Genius(API_KEY)
public = PublicAPI()
#genius = Genius(API_KEY)


list_1 = []
list_2 = []
list_3 = []
list_4 = []



def song_functions():
  artist = genius.search_artist("SZA", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  #list_1 = artist.songs
  artist.save_lyrics()
  artist = genius.search_artist("A Boogie wit da Hoodie", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  #list_2 = artist.songs
  artist.save_lyrics()
  artist = genius.search_artist("Lana Del Rey", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  #list_3 = artist.songs
  artist.save_lyrics()
  artist = genius.search_artist("Taylor Swift", max_songs = 25, sort = 'popularity')
  #print(artist.songs)
  #list_4 = artist.songs
  artist.save_lyrics()
  return list_1, list_2, list_3, list_4


# create table
def new_tables(cur, conn):
  cur.execute("CREATE TABLE IF NOT EXISTS Genius (full_title TEXT PRIMARY KEY, name TEXT, year INT, id INT)")
  cur.execute("CREATE TABLE IF NOT EXISTS GeniusArtists (name TEXT PRIMARY KEY, artistid INT)")
  conn.commit()

# add data into table
def input_data(cur, conn):
  f = open("Lyrics_SZA.json")
  data = f.read()
  f.close()
  data_2 = json.loads(data)
  cur.execute("SELECT count(*) from Genius")
  count = cur.fetchone()[0]
  if count == None:
    count = 0
  for item in range(count, count + 25):
    try:
      title_column = data_2["songs"][item]["full_title"]
      name_column = data_2["name"]
      year_column = data_2["songs"][item]["release_date_components"]["year"]
      artist_id_column = data_2["id"]
      cur.execute("INSERT OR IGNORE INTO Genius (full_title, name, year, id) VALUES (?, ?, ?, ?)", (title_column, name_column, year_column, artist_id_column))
    except:
      "Exceeded 25 rows"
  conn.commit()

  #def add_data_1(cur, conn): 
  f = open("Lyrics_SZA.json")
  data = f.read()
  f.close()
  data_2 = json.loads(data)
  for item in range(0, 25):
    title_column = data_2["songs"][item]["full_title"]
    name_column = data_2["name"]
    year_column = data_2["songs"][item]["release_date_components"]["year"]
    artist_id_column = data_2["id"]
    cur.execute("INSERT or IGNORE INTO Genius (full_title, name, year, id) VALUES (?, ?, ?, ?)", (title_column, name_column, year_column, artist_id_column))
  conn.commit()

  def add_data_2(cur, conn): 
    f = open("Lyrics_LanaDelRey.json")
    data = f.read()
    f.close()
    data_3 = json.loads(data)
    for item in range(0, 25):
      title_column = data_3["songs"][item]["full_title"]
      name_column = data_3["name"]
      year_column = data_3["songs"][item]["release_date_components"]["year"]
      artist_id_column = data_3["id"]
      cur.execute("INSERT or IGNORE INTO Genius (full_title, name, year, id) VALUES (?, ?, ?, ?)", (title_column, name_column, year_column, artist_id_column))
    conn.commit()

  def add_data_3(cur, conn): 
    f = open("Lyrics_ABoogiewitdaHoodie.json")
    data = f.read()
    f.close()
    data_4 = json.loads(data)
    for item in range(0, 25):
      title_column = data_4["songs"][item]["full_title"]
      name_column = data_4["name"]
      year_column = data_4["songs"][item]["release_date_components"]["year"]
      artist_id_column = data_4["id"]
      cur.execute("INSERT or IGNORE INTO Genius (full_title, name, year, id) VALUES (?, ?, ?, ?)", (title_column, name_column, year_column, artist_id_column))
    conn.commit()

  def add_data_4(cur, conn): 
    f = open("Lyrics_TaylorSwift.json")
    data = f.read()
    f.close()
    data_5 = json.loads(data)
    for item in range(0, 25):
      title_column = data_5["songs"][item]["full_title"]
      name_column = data_5["name"]
      year_column = data_5["songs"][item]["release_date_components"]["year"]
      artist_id_column = data_5["id"]
      cur.execute("INSERT or IGNORE INTO Genius (full_title, name, year, id) VALUES (?, ?, ?, ?)", (title_column, name_column, year_column, artist_id_column))

    # artist table for SZA
  def add_data_5(cur, conn):
    f = open("Lyrics_SZA.json")
    data = f.read()
    f.close()
    data_2 = json.loads(data)
    for item in range(0, 25):
      name_column = data_2["name"]
      artist_id_column = data_2["id"]
      cur.execute("INSERT OR IGNORE INTO GeniusArtists (name, id) VALUES (?, ?)", (name_column, artist_id_column))
      conn.commit()

    # artist table for LanaDelRey
  def add_data_6(cur, conn):
    f = open("Lyrics_LanaDelRey.json")
    data = f.read()
    f.close()
    data_3 = json.loads(data)
    for item in range(0, 25):
      name_column = data_3["name"]
      artist_id_column = data_3["id"]
      cur.execute("INSERT OR IGNORE INTO GeniusArtists (name, id) VALUES (?, ?)", (name_column, artist_id_column))
      conn.commit()
    
    # artist table for ABoogiewitdaHoodie
  def add_data_7(cur, conn):
    f = open("Lyrics_ABoogiewitdaHoodie.json")
    data = f.read()
    f.close()
    data_4 = json.loads(data)
    for item in range(0, 25):
      name_column = data_4["name"]
      artist_id_column = data_4["id"]
      cur.execute("INSERT OR IGNORE INTO GeniusArtists (name, id) VALUES (?, ?)", (name_column, artist_id_column))
      conn.commit()
    # artist table for Taylor Swift
  def add_data_8(cur, conn):
    f = open("Lyrics_TaylorSwift.json")
    data = f.read()
    f.close()
    data_5 = json.loads(data)
    for item in range(0, 25):
      name_column = data_5["name"]
      artist_id_column = data_5["id"]
      cur.execute("INSERT OR IGNORE INTO GeniusArtists (name, id) VALUES (?, ?)", (name_column, artist_id_column))
      conn.commit()
  
#def read_data_in_json(files):
    #full_path = os.path.join(os.path.dirname(__file__), files)
    #f = open(full_path)
    #file_data = f.read()
    #f.close()
    #json_data = json.loads(file_data)
    #return json_data

#def writing_json(files,dict):
    #jsonString = json.dumps(dict)
    #with open(files, 'w') as outFile:
        #outFile.write(jsonString)

#def make_visualizations_hist(cur, conn):
    #cur.execute("SELECT name,year from Genius")
    #result = cur.fetchall()
    #conn.commit()
    
    #x_values = []
    #for values in result:
      #x_values.append(values[1])
    #fig, ax = plt.subplots(figsize =(10, 7))

    #ax.hist(mean(x_values), bins = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
    #plt.title("Average Year Top Songs Were Produced")
    #plt.xlabel("Mean of Year")
    #plt.ylabel("Number of Occurences")
    #plt.show()

    #df = px.artist.year()
    #fig = px.histogram(df, x="year", category_orders=dict(year=[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]))
    #fig.show()
  

# Write the json data to a file 
#def writing_json_genius(files,dict):
    #jsonString = json.dumps(dict)
    #with open(genius.py, 'w') as outFile:
        #outFile.write(jsonString)
    
    #for year_var in year_column[data_2]:
  
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
