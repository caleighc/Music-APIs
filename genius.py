from operator import itemgetter
import unittest
import sqlite3
import requests, json
import os
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import plotly.express as px
import csv

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
genius.timeout = 20



list_1 = []
list_2 = []
list_3 = []
list_4 = []



def song_functions():
  artist = genius.search_artist("SZA", max_songs = 25, sort = 'popularity')
  print(artist.songs)
  #artist.save_lyrics()
  #print(artist)
  print(artist.songs)
  #list_1 = artist.songs
  artist = genius.search_artist("A Boogie wit da Hoodie", max_songs = 25, sort = 'popularity')
  print(artist.songs)
  # #list_2 = artist.songs
  #artist.save_lyrics()
  artist = genius.search_artist("Lana Del Rey", max_songs = 25, sort = 'popularity')
  print(artist.songs)
  # #list_3 = artist.songs
  #artist.save_lyrics()
  artist = genius.search_artist("Taylor Swift", max_songs = 25, sort = 'popularity')
  print(artist.songs)
  # #list_4 = artist.songs
  #print(artist.songs)
  # return list_1, list_2, list_3, list_4


# create table
def new_tables(cur, conn):
  cur.execute("CREATE TABLE IF NOT EXISTS Genius (full_title TEXT PRIMARY KEY, year INT, id INT)")
  cur.execute("CREATE TABLE IF NOT EXISTS GeniusArtists (name TEXT PRIMARY KEY, id INT)")
  conn.commit()

 
#  # make list of all songs in order to get 25 at a time
# def list_of_tuples(item, cur, conn):
#   #create an empty list to store the tuples
#   group_of_tuples = []
#   #open the Lyrics_SZA.json file and read its contents into a variable
#   with open("Lyrics_SZA.json") as f:
#     data_2 = json.load(f)
#     cur.execute("SELECT count(*) from Genius")
#     count = cur.fetchone()[0]
#     if count == None:
#       count = 0
#     for item in range(count, count + 25):
#         title_column = data_2["songs"][item]["full_title"]
#         year_column = data_2["songs"][item]["release_date_components"]["year"]
#         artist_id_column = data_2["id"]
#         group_of_tuples.append((title_column, year_column, artist_id_column))
#   with open("Lyrics_LanaDelRey.json") as f:
#     data_3 = json.load(f)
#     title_column = data_3["songs"][item]["full_title"]
#     year_column = data_3["songs"][item]["release_date_components"]["year"]
#     artist_id_column = data_3["id"]
#     group_of_tuples.append((title_column, year_column, artist_id_column))
#   with open("Lyrics_ABoogiewitdaHoodie.json") as f:
#     data_4 = json.load(f)
#     title_column = data_4["songs"][item]["full_title"]
#     year_column = data_4["songs"][item]["release_date_components"]["year"]
#     artist_id_column = data_3["id"]
#     group_of_tuples.append((title_column, year_column, artist_id_column))
#   with open("Lyrics_TaylorSwift.json") as f:
#     data_5 = json.load(f)
#     title_column = data_5["songs"][item]["full_title"]
#     year_column = data_5["songs"][item]["release_date_components"]["year"]
#     artist_id_column = data_5["id"]
#     group_of_tuples.append((title_column, year_column, artist_id_column))
#   print(group_of_tuples)



#   for file in list_of_file_names:
#     f = open
#     data = f.read()
#   f.close()
#   #append each group of information into a list of tuples




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
    title_column = data_2["songs"][item]["full_title"]
    year_column = data_2["songs"][item]["release_date_components"]["year"]
    artist_id_column = data_2["id"]
    cur.execute("INSERT OR IGNORE INTO Genius (full_title, year, id) VALUES (?, ?, ?)", (title_column, year_column, artist_id_column))
  conn.commit()

  
  f = open("Lyrics_LanaDelRey.json")
  data = f.read()
  f.close()
  data_3 = json.loads(data)
  for item in range(count, count + 25):
    title_column = data_3["songs"][item]["full_title"]
    year_column = data_3["songs"][item]["release_date_components"]["year"]
    artist_id_column = data_3["id"]
    cur.execute("INSERT or IGNORE INTO Genius (full_title, year, id) VALUES (?, ?, ?)", (title_column, year_column, artist_id_column))
    conn.commit()

  #def add_data_3(cur, conn): 
  f = open("Lyrics_ABoogiewitdaHoodie.json")
  data = f.read()
  f.close()
  data_4 = json.loads(data)
  for item in range(0, 25):
    title_column = data_4["songs"][item]["full_title"]
    year_column = data_4["songs"][item]["release_date_components"]["year"]
    artist_id_column = data_4["id"]
    cur.execute("INSERT or IGNORE INTO Genius (full_title, year, id) VALUES (?, ?, ?)", (title_column, year_column, artist_id_column))
    conn.commit()

  #def add_data_4(cur, conn): 
  f = open("Lyrics_TaylorSwift.json")
  data = f.read()
  f.close()
  data_5 = json.loads(data)
  for item in range(0, 25):
    title_column = data_5["songs"][item]["full_title"]
    year_column = data_5["songs"][item]["release_date_components"]["year"]
    artist_id_column = data_5["id"]
    cur.execute("INSERT or IGNORE INTO Genius (full_title, year, id) VALUES (?, ?, ?)", (title_column, year_column, artist_id_column))
    conn.commit()

  #artist table for SZA
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

  #artist table for LanaDelRey
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
  
# def read_data_in_json(files):
#     full_path = os.path.join(os.path.dirname(__file__), files)
#     f = open(full_path)
#     file_data = f.read()
#     f.close()
#     json_data = json.loads(file_data)
#     return json_data

# def writing_json(files,dict):
#     jsonString = json.dumps(dict)
#     with open(files, 'w') as outFile:
#         outFile.write(jsonString)


#calculate the average amount of words in top four artists' most popular songs
def calculation(cur, conn):
  cur.execute("SELECT id FROM GeniusArtists")
  artist_ids = cur.fetchall()
  artist_id_word_counts = {}
  for artist_id in artist_ids:
    cur.execute("SELECT id FROM Genius WHERE id=?", (artist_id[0],))
    titles = cur.fetchall()
    word_counts = []
    for title in titles:
      word_counts.append(len(title[0].split(" ")))
    if word_counts:
      average_word_count = sum(word_counts) / len(word_counts)
    else:
      average_word_count = 0
    artist_id_word_counts[artist_id[0]] = average_word_count
  return artist_id_word_counts

  
  # cur.execute("SELECT full_title FROM Genius")
  # titles = cur.fetchall()
  # if not titles:
  #   print("The Genius table is empty.")
  #   return
  # word_counts = []
  # for title in titles:
  #   word_counts.append(len(title[0].split(" ")))
  # if word_counts:
  #   average_word_count = sum(word_counts) / len(word_counts)
  # else:
  #   average_word_count = 0
  # return average_word_count
  # conn.commit()


def write_to_csv_new_file_1(artist_id_word_counts):
  headers = ["Artist ID", "Average Amount of Words in Song Title"]
  rows = []
  for artist_id, word_count in artist_id_word_counts.items():
    rows.append([id, word_count])
  with open("new_file_1.csv", "w+", newline="") as f:
    write = csv.writer(f, delimiter=',')
    write.writerow(headers)
    write.writerows(rows)

 #Read the data from the CSV file into a list called `data`
def make_visualizations_hist(cur, conn):
  with open("new_file_1.csv", "r") as f:
    reader = csv.reader(f)
    data = [row[1] for row in reader][1:]  # Skip the first row (the headers)

# Create the histogram using Matplotlib's hist function
plt.hist(data)
plt.show()
  
  
  
  # headers = ["Artist ID", "Average Amount of Words in Song Title"]
  # rows = [[1, average_word_count]]
  # with open("new_file_1.csv", "w+", newline = "") as f:
  #   write = csv.writer(f, delimiter = ',')
  #   write.writerow(headers)
  #   write.writerows(rows)

  
  # cur.execute("SELECT full_title FROM Genius")
  # word_counts = []
  # for title in cur.fetchall():
  #   word_counts.append(len(title.split()))
  #   average_word_count = mean(word_counts)
  #   answer = cur.fetchall()
  # print(f"Average number of words in song titles: {average_word_count}")
   


    
    



