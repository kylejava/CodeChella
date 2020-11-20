import keys as s
import tweepy
import json
import webbrowser
from pprint import pprint


#Replace Keys with Final Twitter Account
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
api = tweepy.API(auth)


# Grabs the picture from the last mentioned tweet
mentions = api.mentions_timeline()
for mention in mentions:
    pic = (mention.entities['media'][0]['media_url'])
    break



webbrowser.open(pic)
