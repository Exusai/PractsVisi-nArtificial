import cv2 as cv
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Load the image in black and white
I = cv.imread("imgs/edif1.jpg")

# Add blur to the image
#I = cv.GaussianBlur(I, (5, 5), 0)

Iorg = I.copy()

# Convert to gray scale
I = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

# Derivadas
Ix = np.diff(I, axis=0, prepend=0)
Ixx = np.diff(Ix, axis=0, prepend=0)
Iy = np.diff(I, axis=1, prepend=0)
Iyy = np.diff(Iy, axis=1, prepend=0)
Ixy = np.diff(Ix, axis=1, prepend=0)

# Esquinosidad
#K = (Ixx*Iy**2 + Iyy*Ix**2 - 2*Ixy*Ix*Iy)/(Ix**2 + Iy**2)
num = (Ixx*Iy**2 + Iyy*Ix**2 - 2*Ixy*Ix*Iy)
den = (Ix**2 + Iy**2)

response = np.zeros_like(I)

mask = den != 0
response[mask] = num[mask] / den[mask]

""" plt.imshow(response)
plt.show() """

#tr = np.average(response) + 2*np.std(response)
tr = np.max(response)*.8
bin = np.where(response > tr, 255, 0)

""" plt.imshow(bin)
plt.show() """

# get a list of points where det is greater than 0
points = np.where(bin > 0)

#iterate over the list of points and get the coordinates of the points
for i in range(len(points[0])):
    cv.circle(Iorg, (points[1][i], points[0][i]), 1, (0, 0, 255), -1)

# display the image
cv.imshow("Img", Iorg)
cv.waitKey(0)