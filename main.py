import keys as s
import tweepy
import json
import webbrowser
import time
from pprint import pprint
import os, io
from google.cloud import vision
import sys
import requests
from test import *

#from google.cloud import storage
#from google.cloud.vision_v1 import enums
#from google.cloud.vision_v1 import ImageAnnotatorClient
#from google.cloud.vision_v1 import types

#Replace Keys with Final Twitter Account
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
api = tweepy.API(auth)

#Transfers the image to the Google Vision api
def identifyImage(image_from_tweet):
    image = 'https://www.mountroyalseeds.com/wp-content/uploads/2016/09/Abies-lasiocarpa_2-480x640.jpg'
    client = vision.ImageAnnotatorClient()
    response = client.annotate_image({
  'image': {'source': {'image_uri': image}},
  'features': [{'type': vision.enums.Feature.Type.FACE_DETECTION}],})
    print(response)



# Grabs the picture from the last mentioned tweet'
def searchForImages():
    mentions = api.mentions_timeline()
    for mention in mentions:
        if('#roots' in mention.text):
            print(mention.user.screen_name)
            api.status_update('@' + mention.user.screen_name+ " test worked")
