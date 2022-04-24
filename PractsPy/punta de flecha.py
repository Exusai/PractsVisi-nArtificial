import cv2 as cv
import numpy as np

img = cv.imread('imgs/LennaRGB.png', 1)
imgCopy = img.copy()

cv.imshow('Colores', imgCopy)


def colores(event, x,y, flag, param):
    global img
    if event == cv.EVENT_LBUTTONDOWN:
        color = img[x,y].tolist()
        print('BGR:', color)
        #cv.circle(img, (x,y), 40, color, -1)
        cv.arrowedLine(img, (0,0), (x,y), (0,0,255), 4)
    elif event == cv.EVENT_LBUTTONUP:
        img = imgCopy.copy()

    cv.imshow('Colores', img)

cv.setMouseCallback('Colores', colores)
cv.waitKey(0)
cv.destroyAllWindows()