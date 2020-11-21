#testing how to reply back to tweets containing key words
import notATest as s
import tweepy
import time
import json
from pprint import pprint
import requests
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)

api = tweepy.API(auth)

for i in range (0, 10):
    if i%2 == 0:
        api.update_status("@kylejava2 #roots test"+ str (i))
    else:
        api.update_status("@kylejava2 test" + str (i))

#function to download image
def download_image(path, url):
    with requests.get(url, stream=True) as r:
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
