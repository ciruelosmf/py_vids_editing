import re

# Get the response text.
with open('text_etsy_store.txt', 'r') as f:
    content = f.read()

f.close()
# response_text = my_response.text

# Split the response text into paragraphs.
paragraphs = re.split(r'\n', content)

# Create a list with the paragraphs.
paragraph_list = []
for paragraph in paragraphs:
    paragraph_list.append(paragraph)

# Print the paragraph list.
print(paragraph_list)

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import textwrap 


# Get the list of paragraphs.
paragraphs = paragraph_list

# Iterate over the list of paragraphs.
for i, paragraph in enumerate(paragraphs):
    t = textwrap.fill(paragraph)
    # If the paragraph is empty, skip it.
    if paragraph == '':
        continue

    # Create a blank image.
    image = Image.new("RGB", (800, 500), color=(165, 255, 255))

    # Write the paragraph to the image.
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("impact.ttf", 22)
    w, h = draw.textsize(t, font=font)
    draw.text((800 // 2 - (w // 2) +2, 500 // 2 - h // 2), t, fill=(0, 0, 0), font=font,spacing=17)

    # Save the image.
    image.save(f"output_{i}.png")
    image.save(f"output_{i}.png")