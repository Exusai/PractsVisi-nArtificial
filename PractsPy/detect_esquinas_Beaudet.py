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

# x derivative
sobelx = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

#y derivative
sobely = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

#Ixx = signal.convolve2d(signal.convolve2d(I, sobelx, "same"),sobelx,"same")     
#Iyy = signal.convolve2d(signal.convolve2d(I, sobely, "same"),sobely,"same")
#Ixy = signal.convolve2d(signal.convolve2d(I, sobelx, "same"),sobely,"same")

Ix = np.diff(I, axis=0, prepend=0)
Ixx = np.diff(Ix, axis=0, prepend=0)

Iy = np.diff(I, axis=1, prepend=0)
Iyy = np.diff(Iy, axis=1, prepend=0)

Ixy = np.diff(Ix, axis=1, prepend=0)

""" plt.imshow(Ixx, cmap='gray')
plt.show()

plt.imshow(Iyy, cmap='gray')
plt.show()

plt.imshow(Ixy, cmap='gray')
plt.show() """

# Operator
det = Ixx*Iyy - Ixy**2

# get local maxima of det matrix in a 10x10 neighborhood
#det_max = signal.convolve2d(det, np.ones((10, 10)), "same")

""" plt.imshow(det_max)
plt.show() """

# binarize the matrix det
tr = np.average(det) + 2*np.std(det)
#tr = .1*np.max(det)

bin = np.where(det > tr, 255, 0)

""" ellipticPoints = np.where(det > 0, 255, 0)
hyperbolicPoints = np.where(det < 0, 255, 0)
parabolicPoints = np.where(det == 0, 255, 0) """

""" plt.imshow(hyperbolicPoints)
plt.show() """

# get a list of points where det is greater than 0
points = np.where(bin > 0)

#iterate over the list of points and get the coordinates of the points
for i in range(len(points[0])):
    cv.circle(Iorg, (points[1][i], points[0][i]), 1, (0, 0, 255), -1)

# display the image
cv.imshow("Img", Iorg)
cv.waitKey(0)