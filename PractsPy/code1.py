import cv2
import numpy as np

im = cv2.imread("lennaRGB.png")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("img", im)
#cv2.waitKey(0)

cv2.imshow("img2", gray)
cv2.waitKey(0)

cv2.destroyAllWindows()

print("Hello")