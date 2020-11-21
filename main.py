#import keys as s
import tweepy
import json
import webbrowser
import time
from pprint import pprint
import requests

#Replace Keys with Final Twitter Account
#auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
#auth.set_access_token(s.access_token, s.access_token_secret)
#api = tweepy.API(auth)


"""
Function used to download images
path, url are passed in from the searchForImages()
"""

def download_image():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/220px-Image_created_with_a_mobile_phone.png"
    path = 'image.png'
    with requests.get(url, stream=True) as r:
        content = b''
        for chunk in r.iter_content(chunk_size=8192):
              content = content + chunk

        print(content)


"""
 Grabs the picture from the last mentioned tweet
 TODO: Finish this function
"""
#def searchForImages():
#    mentions = api.mentions_timeline()
#    for mention in mentions:
#        if('#roots' in mention.text):
#            ent = (mention.entities)
#            image = (ent['media'][0]['media_url'])
            #download_image('/' , url)
download_image()

