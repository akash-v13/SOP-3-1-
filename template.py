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
    

def edge():
    img = cv2.imread("half.png")
    edges = cv2.Canny(img,100,200)
    plt.ioff()

    plt.subplot(121), plt.imshow(img,cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges,cmap='gray')
    plt.title('Post Detection'), plt.xticks([]), plt.yticks([])

    plt.show()

if __name__ == "__main__":
    whitenoise()
    edge()
