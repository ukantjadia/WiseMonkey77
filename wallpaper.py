#!/usr/bin/env python3

from PIL import Image ,ImageDraw, ImageFont
#import Pillow
import textwrap
from bot import *

def get_image(quote,author):
    image = Image.new('RGB',(800,500),color=(0,0,0))
    font = ImageFont.truetype("NRegular.ttf",40)
    text_color = (200,200,200)
    test_start_height = 70
    write_text_on_image(image,quote,author,font,text_color,test_start_height)
    image.save('quoteImg.png')

def write_text_on_image(image,text,author,font,text_color,text_start_height):
    draw = ImageDraw.Draw(image)
    image_width,image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text,width=30)
    print(lines)
    for line in lines:
        line_width,line_height = font.getsize(line)
        draw.text(((image_width - line_width)/2,y_text),line,font=font,fill=text_color)
        y_text += line_height
        print("y_text= ",y_text)

    draw.text((390,y_text+20),author,font=font,fill=text_color)
    print("")
    crop_img(image,y_text)
    print("y_text= ",y_text+20)

def crop_img(image,y_text,):
    print(y_text)
    size = image.size
    print(size[1])
    bottom = (size[0] -( y_text + 70 ))
    top = 20
    left = 50
    right = 60
    croped = image.crop((left,top,right,bottom))
    return image
