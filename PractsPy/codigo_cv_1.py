import cv2 as cv
import numpy as np

def new_func():
    im = cv.imread("lennaRGB.png")
    return im

img = new_func()
cv.imshow("img", img)

img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("img2", img2)


cv.waitKey(0)
cv.destroyAllWindows()

