#!/usr/bin/env python3

import tweepy
from wallpaper import get_image
from bot import *

#### uploading the file for tweet

# getting the tweet
def upload(quote,author,tag):
    #quote = get_quote() 
    get_image(quote,author)
    print(quote)
    media = api.simple_upload('quoteImg.png')
    #tweet =["#quoteOfTheDay ",tag , " #qod"]
    tweet1 ="#QuoteOfTheDay ""#qod " "#quotes " "#quotesandsayings " "#quoteof " "#QotD " 
    tag1= " #"+"".join(tag)

    tweet ="".join((tweet1,tag1))

    post_result = api.update_status(status=tweet,media_ids=[media.media_id])

