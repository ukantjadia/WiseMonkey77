#!/usr/bin/env python3

import tweepy
import configparser

#config=configparser.ConfigParser()
#config.read('config.ini')
doc = open('/WiseMonkey77/key.txt','r').read().splitlines()


#api_key=config['twitter']['api_key']
#api_sceret=config['twitter']['api_sceret']
#access_token=config['twitter']['access_token']
#access_token_sceret=config['twitter']['access_token_sceret']

api_key=doc[0]
api_sceret=doc[1]
access_token=doc[2]
access_token_sceret=doc[3]

# Using class OAuthHandler to authenticate
auth = tweepy.OAuthHandler(api_key,api_sceret)
auth.set_access_token(access_token,access_token_sceret)

# Creating object to access different modules of twitter api
api = tweepy.API(auth)


#### Verification(static) code complete



## verifying the credentials
#try: api.verify_credentials()
#    print("everything is ok")
#except:
#    print("authentication error")
