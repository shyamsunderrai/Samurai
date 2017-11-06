#!/usr/bin/env python

from twitter import *
import json

config = {}
execfile("config.py", config)

twitter = Twitter( auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
query = twitter.search.tweets(q = input("Enter Search String: "))

def inputstring():
   for result in query["statuses"]:
      #tweetstring = "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
      #print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
      #tweetstring = "%s,%s,%s" % (result["created_at"], result["user"]["screen_name"], result["text"])

      tweetstring = "%s,%s,%s"% (result["created_at"], result["user"]["screen_name"], result["text"])
      process_strip = tweetstring.strip()
      print process_strip
      
inputstring()
