#!/usr/bin/env python

__author__= 'Shyam Rai'

## Assuming that Your mongodb is running locally and listening at Port 27017

import pymongo

uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(uri)
database = client['test']
collection = database['tweet']

tweets = collection.find({})
for tweet in tweets:
   print tweet 
