import unittest
import sqlite3
import requests, json
import os
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import plotly.express as px
from audio import *

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

import requests
def newsongs():
    url = "https://genius-song-lyrics1.p.rapidapi.com/artists/111352/songs"

    querystring = {"sort":"title","per_page":"20","page":"1"}

    headers = {
	    "X-RapidAPI-Key": "2d60a2dc02msh14643c57beca02ep15b0dajsn8516bf66b65c",
	    "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


