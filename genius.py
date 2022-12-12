import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import numpy as np

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

def set_up_db(db_name):
  path = os.path.dirname(os.path.abspath(__file__))
  conn = sqlite3.connect(path+'/'+db_name)
  cur = conn.cursor()
  return cur,conn
set_up_db("music.db")

# create table
def new_tables(cur, conn):
  # cur.execute('DROP TABLE IF EXISTS Genius')
  cur.execute("CREATE TABLE IF NOT EXISTS Genius (full_title TEXT PRIMARY KEY, name TEXT, year INTEGER)")
  conn.commit()

#f = open ('Lyrics_SZA.json', "r")
#data  = json.loads(f.read())
#for i in data:
  #print(i)
ARTIST_NAME = "<SZA>"
def _get(path, params=None, headers=None):
  requrl = '/'.join([BASE_URL, path])
  token = "Bearer {}".format(API_KEY)
  if headers:
    headers['Authorization'] = token
  else:
    headers = {"Authorization": token}
  
  response = requests.get(url=requrl, params=params, headers=headers)
  response.raise_for_status()

  return response.json

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

# Write the json data to a file 
def writing_json(filename,dict):
    jsonString = json.dumps(dict)
    with open(filename, 'w') as outFile:
        outFile.write(jsonString)

   
def make_visualizations(cur,conn):
    plt.figure()
    cur.execute()
    """
    SELECT full_title, avg(year)
    FROM Genius
    """
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
    plt.xlabel('full_title')
    plt.ylabel('year')
    plt.title("full_title vs. year")
    plt.scatter(x,y,color='blue')
    plt.plot(x,line_best_fit, color='red')
    plt.show()
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

def main():
  song_functions()
  cur, conn = set_up_db("music.db")
  new_tables(cur, conn)
  add_data_1(cur, conn)
  add_data_2(cur, conn)
  add_data_3(cur, conn)
  add_data_4(cur, conn)

if __name__ == "__main__":
  main()

