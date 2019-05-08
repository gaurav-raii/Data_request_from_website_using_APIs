# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:48:46 2019

@author: gaura
"""
import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}