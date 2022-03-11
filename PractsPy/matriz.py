import cv2 as cv
import numpy as np

matriz = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

img1 = np.array(matriz)
img1 = np.uint8(matriz)

print(img1)
print('Método 1')

img2 = np.zeros((5,4), np.uint8)
print(img2)
print('Método 2')

alto = 1000
ancho = 1000
img3 = np.ones((alto,ancho), np.uint8)*255
cv.imshow("test",img3)
#cv.waitKey(0)

alto2 = 500
ancho2 = 500
img4 = np.ones((alto2,ancho2, 3), np.uint8)*255
img4[:] = (255, 0, 0)
print(img4.shape)
cv.imshow("test2",img4)
cv.waitKey(0)
