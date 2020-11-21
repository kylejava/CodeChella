import keys as s
import tweepy
import json
import webbrowser
import time
from pprint import pprint
import requests
from test.predict import *
from calscaper.calscraper import *
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
    #take this out later
    url = 'https://alchetron.com/cdn/abronia-maritima-06132f4d-5ecb-4acf-bf23-5a2b474fe6e-resize-750.jpg'
    path = 'image.png'
    with requests.get(url, stream=True) as r:
        content = b''
        for chunk in r.iter_content(chunk_size=8192):
              content = content + chunk

        name = get_prediction(content, project_id, model_id)
        desc = parse_sentence(name)
        resp = {
            'name': name,
            'desc': desc
        }
        return(resp)



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
            plant = download_image(image, s.project_id, s.model_id)
            pprint(plant)
            #print("@" + mention.user.screen_name + " That is a " + x)
            #api.update_status(("@" + mention.user_scren_name + x['name'] + "\n" + x['desc']),mention.id)


searchForImages()
