"""
Filtros no lineales
"""

import cv2 as cv
import numpy as np
from scipy.ndimage import *

im = cv.imread('lenaNoise.png', 1)

imgGray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

mask = 7

""" imMax = maximum_filter(imgGray, size=mask)  #scipy.ndimage
cv.imshow('Filtro maximos', imMax)


imMax = minimum_filter(imgGray, size=mask)  #scipy.ndimage
cv.imshow('Filtro minimos', imMax)

imMax = median_filter(imgGray, size=mask)  #scipy.ndimage
cv.imshow('Filtro promedio', imMax) """

cv.namedWindow('Lena', cv.WINDOW_NORMAL)
cv.moveWindow('Lena',0,0)
cv.arrowedLine(im, (200,100), (320,300), (255,0,255), 4)
cv.imshow('Lena', im)

cv.waitKey(0)
cv.destroyAllWindows()