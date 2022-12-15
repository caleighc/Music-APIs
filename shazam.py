import requests
import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import plotly.express as px
from lyricsgenius import API, PublicAPI, Genius



# Requesting data from Shazam API key
def top_100(Country_code):
    url = "https://shazam-core.p.rapidapi.com/v1/charts/country"
    querystring = {"country_code":Country_code,"offset":"100"}
    headers = {
	    "X-RapidAPI-Key": "2d60a2dc02msh14643c57beca02ep15b0dajsn8516bf66b65c",
	    "X-RapidAPI-Host": "shazam-core.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    details = response.text

    info_list = json.loads(details)
    created_list = []

    rank = 1
    for item in info_list:
        #tuple = (item['title'], get_artists(item['artists']), rank)
        created_list.append(tuple)
        rank+=1
    print(created_list)
    return created_list
   



#def get_artists(artists):
    #created_list = []
    #if artists != None:
        #for exist in artists:
            #created_list.append(exist['alias'])
            #return created_list
        #else:
            #created_list.append('Unknown')
            #return created_list

#def num_times_artists_show_up(US_top100):
    #artist_list = {}
    # Iterates through a list 
    #for song in US_top100:
        # Iterates through a tuple
        #for art in song[1]:
            # Checks to see if the artist is already in the dict 
            #if not art in artist_list.keys():
                #artist_list[art] = 1
            # if not they are added in with a value of 1
            #else:
                #artist_list[art] = artist_list[art] + 1

            



#url = "https://shazam-core.p.rapidapi.com/v1/tracks/total-shazams"

#querystring = {"track_id":"469270443", "offset":"100"}

#headers = {
	#"X-RapidAPI-Key": "87bfb8f528mshda7e9ea907b3760p11367ajsnf8556282acb7",
	#"X-RapidAPI-Host": "shazam-core.p.rapidapi.com"
#}

#response = requests.request("GET", url, headers=headers, params=querystring)
