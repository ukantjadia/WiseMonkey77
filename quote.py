#!/usr/bin/env python3

import requests
import json

def get_quote():
    URL = "https://api.quotable.io/random"
    try:
        response = requests.get(URL)
    except:
        print("ERROR during fetching quote")

    res = json.loads(response.text)
    print(res)
   # return res['content']+"--\n"+res['author']
   # return res['tag']
    return res['content'],"-- "+res['author'],res['tags']
