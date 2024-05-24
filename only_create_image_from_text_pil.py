 

import numpy as np

from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *

# Create a transparent image
img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))

# Add text to the image
font_size = 50
with open('text_file.txt', 'r') as file:
    text = file.read()
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', font_size)
#text = 'In 1965, Mariner 4 \nmade history \nas the first spacecraft \nto flyby Mars. \nBut that\n is not all. \nIn 1971, Mariner 9 \nwas launched \nand became \nthe first spacecraft \nto orbit the \nred planet.'

text_width, text_height = draw.textsize(text, font)
while text_width > img.width or text_height > img.height:
    font_size -= 2
    font = ImageFont.truetype('arial.ttf', font_size)
    text_width, text_height = draw.textsize(text, font)

x = (img.width - text_width) // 2
y = (img.height - text_height) // 2
draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
img.show()

"""



"""
