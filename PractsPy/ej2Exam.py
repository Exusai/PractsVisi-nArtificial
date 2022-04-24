import cv2 as cv
from scipy import ndimage
from skimage import filters
import numpy as np
import matplotlib.pyplot as plt


# leer img
ath = cv.imread('imgs/ath.jpg', 1)
vader = cv.imread('imgs/vader.jpg', 1)

alpha = .5

ath = np.asanyarray(ath)/255 * alpha
vader = np.asanyarray(vader)/255 * alpha

print(ath.shape)
print(vader.shape)
sum = ath[0:1161, 0:1920,:] + vader[0:1161, 0:1920,:]
print(sum.shape)

cv.imshow('suma', sum)
cv.waitKey(0)