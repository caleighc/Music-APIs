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
    # Create tables for genius
   
    # Create tables for apple music 

    # Add data for spotify
    
    # Add data for genius 
    
    # Add data for apple music 


if __name__ == "__main__":
    main()