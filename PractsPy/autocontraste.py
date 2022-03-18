import cv2
import numpy as np

img = cv2.imread("hoja.jpg")

scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 15)

result = img.copy()
result[thresh==255] = (255,255,255)

cv2.imshow("org", img)
cv2.imshow("lim", thresh)
cv2.imshow("ajustada", result)
cv2.waitKey(0)