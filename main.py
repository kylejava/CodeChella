import keys as s
import tweepy
import json
import webbrowser
import time
from pprint import pprint
import requests
from test.predict import *
from google.protobuf.json_format import MessageToJson
#Replace Keys with Final Twitter Account
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
api = tweepy.API(auth)


"""
Function used to download images
path, url are passed in from the searchForImages()
"""

def download_image(url , project_id, model_id):

    path = 'image.png'
    with requests.get(url, stream=True) as r:
        content = b''
        for chunk in r.iter_content(chunk_size=8192):
              content = content + chunk

        x = get_prediction(content, project_id, model_id)
        return(x)



"""
 Grabs the picture from the last mentioned tweet
 TODO: Finish this function
"""
def searchForImages():
    mentions = api.mentions_timeline()
    for mention in mentions:
        if('#roots' in mention.text and 'media' in mention.entities):
            ent = (mention.entities)
            image = (ent['media'][0]['media_url'])
            x = download_image(image, s.project_id, s.model_id)
            print("@" + mention.user.screen_name + " That is a " + x)
            api.update_status(("@" + mention.user.screen_name + " That is a " + x),mention.id)


searchForImages()
