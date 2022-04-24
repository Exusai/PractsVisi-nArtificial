import cv2
import numpy as np

im = cv2.imread("imgs/LennaRGB.png")
#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

b, g, r = cv2.split(im)

""" cv2.imshow("img", im)
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r) """




r1 = im.copy()
r1[:,:,0] = r1[:,:,1] = 0 

cv2.imshow("red", r1)

cv2.waitKey(0)
cv2.destroyAllWindows()