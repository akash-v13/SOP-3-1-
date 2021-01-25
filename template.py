from PIL import Image
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

 

def whitenoise():
    img = Image.open("RowePhantomEye.jpg")
    img = img.convert("RGBA")

    pixdata = img.load()

    for y in range(400):
        for x in range(img.size[0]):
            img.putpixel((x,y),(0,0,0,255))

    for y in range(img.size[1]):
        for x in range(241,272):
            img.putpixel((x,y),(0,0,0,255))
    
    for y in range(img.size[1]):
        for x in range(0,2):
            img.putpixel((x,y),(0,0,0,255))
    
    img.show()
    img.save("half.png")