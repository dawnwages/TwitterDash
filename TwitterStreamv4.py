#Tutorial from https://www.youtube.com/watch?v=pUUxmvvl2FE for Python=2
#Author Dawn Wages
#Last Updated: 7/13/16 3:54 am

""" TwitterStreamv4.py Streaming twitter data and outputing to a csv file based on criteria. """

__author__ = "Dawn Michelle Wages"

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv
import sys
import time

ckey = 'Replace'
csecret = 'Replace'
atoken = 'Replace'
asecret = 'Replace'
#Add title headers
#Add location
#I need a database for this to automatically go to which Tableau will reference
class listener(StreamListener):
    def on_data(self, data):
        try:
            #localtime=time.asctime( time.localtime(time.time()) )
            tweet=data.split(',"text":"')[1].split('","source')[0]
            #author=data.author.screen_name
            #created=data.created_at
            #text=data.text
            #print (localtime, tweet, author, created, text)
            print(tweet)

            
#how are we using time? like when it spits out... i don't get it
#Insert Date and Time of Stream in file name -- HOW?
            #saveThis = str(localtime)+'$'+tweet+'$'+author+'$'+created+'$'+text
            saveThis = time.asctime()+'::'+tweet
            saveFile = open('twitter-data.txt', 'a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except Exception:
        	print ('failed ondata')
        	time.sleep(5)


    def on_error(self, status):
    	print (status)





auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
#What we are filtering our tweets by
twitterStream.filter(track=["dawn"])
