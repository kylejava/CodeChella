import keys as s
import tweepy
import json
import webbrowser
import time
from pprint import pprint


#Replace Keys with Final Twitter Account
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
api = tweepy.API(auth)


# Grabs the picture from the last mentioned tweet'
def searchForImages():
    mentions = api.mentions_timeline()
    for mention in mentions:
        if('#roots' in mention.text):
            print(mention.user.screen_name)
            api.status_update('@' + mention.user.screen_name+ " test worked")


while True:
    searchForImages()
    time.sleep(15)
