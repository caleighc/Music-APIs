import unittest
import sqlite3
import json
import os

# import all our files
import spotify
import genius
import apple

# Set up the database given the db_name
def set_up_db(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def main():
    cur,conn = set_up_db("music.db") 
    # Create tables for spotify 
    spotify.create_artists_table(cur,conn)
    spotify.make_songs_table(cur,conn)
    # Add data for spotify
    playlist_ids = ["37i9dQZF1DX7Jl5KP2eZaS","37i9dQZF1DX0kbJZpiYdZl","6SjN06zZBZpsCWJk2DwhDs","3KHb0WRmzbp9WH7E2mXVmx","0chdKQr18NN9WRI355V8BN"]
    for id in playlist_ids:
        jsonDict = spotify.make_request(id)
        spotify.add_artists_id(jsonDict,cur,conn)
        spotify.add_songs(jsonDict,cur,conn)
    # Create tables for genius
    
    # Add data for genius 
    
    # Create tables for apple music 
    
    # Add data for apple music 


if __name__ == "__main__":
    main()