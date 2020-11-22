import keys as s
import tweepy
import json
import webbrowser
import time
from pprint import pprint
import requests
from auto_ml.predict import *
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
    path = 'image.png'
    with requests.get(url, stream=True) as r:
        content = b''
        for chunk in r.iter_content(chunk_size=8192):
              content = content + chunk

        name = get_prediction(content, project_id, model_id)
        desc = parse_sentence(name)
        link = get_webpage(name)
        resp = {
            'name': name,
            'desc': desc,
            'link': link
        }
        return(resp)

"""
Function is used to check if a given id is in the replied_tweets.txt file
if it is found it will return True otherwise return false
"""
def check_id_in_file(id):
    with open('replied_tweets.txt' , 'r') as read_obj:
        for line in read_obj:
            if(id in line):
                return True

    return False




"""
 Grabs the picture from the last mentioned tweet
 and then returns data to about that plant to the twitter user
"""
def searchForImages():
    mentions = api.mentions_timeline()
    myFile = open('replied_tweets.txt', 'a')
    for mention in mentions:
        mention_id = str(mention.id)
        if(('#roots' in mention.text) and ('media' in mention.entities) and (check_id_in_file(mention_id)== False)):
            ent = (mention.entities)
            image = (ent['media'][0]['media_url'])
            plant = download_image(image, s.project_id, s.model_id)
            myFile.write(str(mention.id))
            myFile.write("\n")
            api.update_status(("@" + mention.user.screen_name + " " + plant['desc']), mention.id)
            api.update_status(("@" + mention.user.screen_name + " Learn more about it here! " + plant['link']), mention.id)
            print("Replied")

    myFile.close()


def main():
    while(True):
        print("Searching for Images")
        searchForImages()
        time.sleep(5)

main()
