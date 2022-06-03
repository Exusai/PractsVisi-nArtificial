import cv2 as cv 
import numpy as np

sombrero = cv.imread('imgs/Sombrero.png')
img = cv.imread('imgs/LennaRGB.png')

talla_sombrero = 1.2

ancho_sombrero, alto_sombrero = sombrero.shape[:2]
ancho_img, alto_img = img.shape[:2]

proporcion_sombrero = ancho_sombrero / alto_sombrero
proporcion_img = ancho_img / alto_img

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

clasificador = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

rostros = clasificador.detectMultiScale(img_gray, 1.3, 5)

for x, y, w, h in rostros:
    #cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    sombrero_resized = cv.resize(sombrero, (w, int(h/2)))

    sombrero_gray = cv.cvtColor(sombrero, cv.COLOR_BGR2GRAY)
    th, threshed = cv.threshold(sombrero_gray, 2, 255, cv.THRESH_BINARY_INV)

    #cv.imshow('Sombrero', threshed)

    # offset sombrero by face height
    offset_x = x + (w - sombrero_resized.shape[1]) // 2
    offset_y = y - sombrero_resized.shape[0] - 10
    img[offset_y:offset_y + sombrero_resized.shape[0], offset_x:offset_x + sombrero_resized.shape[1]] = np.bitwise_and(img[offset_y:offset_y + sombrero_resized.shape[0], offset_x:offset_x + sombrero_resized.shape[1]], sombrero_resized)
    


# display img
cv.imshow('IMG', img)
cv.waitKey(0)
cv.destroyAllWindows()
