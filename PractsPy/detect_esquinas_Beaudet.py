import cv2 as cv
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Load the image in black and white
I = cv.imread("imgs/edif1.jpg", 0)

# Add blur to the image
I = cv.GaussianBlur(I, (5, 5), 0)

# x derivative
sobelx = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

#y derivative
sobely = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

# To get second derivative differentiate twice.
#Ixx = signal.convolve2d(signal.convolve2d(I, sobelx, "same"),sobelx,"same")     
# Iyy  
#Iyy = signal.convolve2d(signal.convolve2d(I, sobely, "same"),sobely,"same")
# Ixy Image 
#Ixy = signal.convolve2d(signal.convolve2d(I, sobelx, "same"),sobely,"same")

Ix = np.diff(I, axis=0, prepend=0)
Ixx = np.diff(Ix, axis=0, prepend=0)

Iy = np.diff(I, axis=1, prepend=0)
Iyy = np.diff(Iy, axis=1, prepend=0)

Ixy = np.diff(Ix, axis=1, prepend=0)

""" plt.imshow(Ixx, cmap='gray')
plt.show() """

""" plt.imshow(Iyy, cmap='gray')
plt.show() """

""" plt.imshow(Ixy, cmap='gray')
plt.show() """

# Get Determinant and trace 
det = Ixx*Iyy - Ixy**2
trace = Ixx + Iyy

# Harris is det(H) - a * trace(H) let a = 0.2 
H = det - 0.2 * trace
det = H

#det = (det)/(1+signal.convolve2d(I, sobelx, "same")**2+signal.convolve2d(I, sobely, "same")**2)**2
#print(kmin.shape)

# binarize the matrix det
tr = np.average(det) + np.std(det)*2
#tr = .1*np.max(det)

bin = np.where(det > tr, 255, 0)

ellipticPoints = np.where(det > 0, 255, 0)
hyperbolicPoints = np.where(det < 0, 255, 0)
parabolicPoints = np.where(det == 0, 255, 0)

""" plt.imshow(hyperbolicPoints)
plt.show() """

# get a list of points where det is greater than 0
points = np.where(bin > 0)

#iterate over the list of points and get the coordinates of the points
for i in range(len(points[0])):
    cv.circle(I, (points[1][i], points[0][i]), 1, (0, 0, 255), -1)

# display the image
cv.imshow("Img", I)
cv.waitKey(0)