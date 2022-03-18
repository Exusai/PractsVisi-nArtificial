import cv2 as cv
from scipy import ndimage
from skimage import filters
import numpy as np
import matplotlib.pyplot as plt
import random

def add_noise(img):
    row , col = img.shape

    number_of_pixels = random.randint(300, 10000)
    for _ in range(number_of_pixels):
       
        y_coord=random.randint(0, row - 1)
         
        x_coord=random.randint(0, col - 1)
         
        img[y_coord][x_coord] = 255

    number_of_pixels = random.randint(300 , 10000)
    for _ in range(number_of_pixels):

        y_coord=random.randint(0, row - 1)
         
        x_coord=random.randint(0, col - 1)
         
        img[y_coord][x_coord] = 0
         
    return img


# leer img
img = cv.imread('coins.jpg', 0)
imgOrg = img.copy()

add_noise(img)


cv.imshow('Ruido', img)

histogram, bin_edges = np.histogram(img, bins=256, range=(0, 255))


#kernel = np.ones((5,5),np.float32)/25
#img = cv.filter2D(img,-1,kernel)

img= cv.medianBlur(img, 3)
cv.imshow('Sin ruido', img)

trUP = 255
trLow = 150

ret,bin = cv.threshold(img, trLow, trUP, cv.THRESH_TOZERO_INV)   #---Binary threshold---

cv.imshow('Segmentada', bin)
cv.imshow('Original', imgOrg)

# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([0.0, 255])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()

#cv.waitKey(0)