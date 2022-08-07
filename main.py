#!/usr/bin/env python3
from bot import *
from quote import get_quote
#from wallpaper import get_image
from twit import upload
#

def main():
    quote,author,tag = get_quote()
    upload(quote,author,tag)



if __name__ == "__main__":
    main()
