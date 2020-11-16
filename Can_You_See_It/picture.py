#!/usr/env/python3
from PIL import Image
import sys, math

video_frame_count = 455846

min_offset = 350*675
max_offset = 550*675

#image_sizes = [640, 800, 1024, 1280, 1360, 1440, 1600, 1680, 1920, 2048, 2560, 3440, 3840]
image_sizes = [1440]
for img_size in image_sizes:
    print(img_size)
    result = Image.new('RGB', (img_size, math.floor((max_offset-min_offset)/img_size)+1))
    j=0
    for i in range(min_offset, max_offset):
        width = i % img_size
        height = j
        print("I: {i}, W: {w}, H: {h}".format(i=i,w=width,h=height))
        pixel = Image.open('frames/{img}.bmp'.format(img=i))
        result.paste(pixel, (width,height))
        if i % img_size == 0:
            j+=1

    print("Writing result...")
    result.save("result_{WIDTH}.bmp".format(WIDTH=img_size))

