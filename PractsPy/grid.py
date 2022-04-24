import cv2 as cv
import numpy as np

# Creando una imagen
#alto = 500
#ancho = 500
#img = np.ones((alto,ancho, 3), np.uint8)*255
#print(img[10,20,:])
#img[:] = (255, 0, 0) #BGR
img = cv.imread("imgs/LennaRGB.png")

# ponendo grid sobre imagen
gridSpacing = 50
colorInBGR = (0, 0, 255)

for j in range(img.shape[0]):
    for k in range(img.shape[1]):
        if (j % gridSpacing) == 0 or (k % gridSpacing) == 0:
            img[j,k,:] = colorInBGR

#print(img.shape)
cv.imshow("test2",img)
cv.waitKey(0)
