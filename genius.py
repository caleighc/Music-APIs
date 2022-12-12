import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import plotly.express as px
# Remi Goldfarb
# Genius API

BASE_URL = "https://api.genius.com"
API_KEY = "HAQwWUcRzMqn3cp-AkOLU0WbsB9bqn4tJ56O_kg8ykbLyYMFoqDgUJ6oxt0MBsuY"
#REDIRECT_URI = "http://localhost"

from lyricsgenius import API, PublicAPI, Genius
genius = Genius(API_KEY)
public = PublicAPI()
genius = Genius(API_KEY)

import requests


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
    
  
#artist = genius.search_artist("Drake", max_songs = 100, sort = 'popularity')
#print(artist.songs)


# create table
def new_tables(cur, conn):
  cur.execute("CREATE TABLE IF NOT EXISTS Genius (full_title TEXT PRIMARY KEY, name TEXT, year INTEGER)")
  conn.commit()


def add_data_1(cur, conn): 
  f = open("Lyrics_SZA.json")
  data = f.read()
  f.close()
  data_2 = json.loads(data)
  for item in range(0, 25):
    title_column = data_2["songs"][item]["full_title"]
    name_column = data_2["name"]
    year_column = data_2["songs"][item]["release_date_components"]["year"]
    cur.execute("INSERT or IGNORE INTO Genius (full_title, name, year) VALUES (?, ?, ?)", (title_column, name_column, year_column))
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
    cur.execute("INSERT or IGNORE INTO Genius (full_title, name, year) VALUES (?, ?, ?)", (title_column, name_column, year_column))
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
    cur.execute("INSERT or IGNORE INTO Genius (full_title, name, year) VALUES (?, ?, ?)", (title_column, name_column, year_column))
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
    cur.execute("INSERT or IGNORE INTO Genius (full_title, name, year) VALUES (?, ?, ?)", (title_column, name_column, year_column))
  conn.commit()
  
def read_data_in_json(files):
    full_path = os.path.join(os.path.dirname(__file__), files)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data

def writing_json(files,dict):
    jsonString = json.dumps(dict)
    with open(files, 'w') as outFile:
        outFile.write(jsonString)

def make_visualizations_hist(cur, conn):
    cur.execute("SELECT artist, avg(year) from Genius")
    result = cur.fetchall()
    conn.commit()
    
    x_values = []
    for values in Genius:
      x_values.append(values[1])
    fig, ax = plt.subplots(figsize =(10, 7))

    ax.hist(mean(x_values), bins = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
    plt.title("Average Year Top Songs Were Produced")
    plt.xlabel("Mean of Year")
    plt.ylabel("Number of Occurences")
    plt.show()

    df = px.artist.year()
    fig = px.histogram(df, x="year", category_orders=dict(year=[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]))
    fig.show()
  

# Write the json data to a file 
def writing_json_genius(files,dict):
    jsonString = json.dumps(dict)
    with open(genius.py, 'w') as outFile:
        outFile.write(jsonString)
    
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
