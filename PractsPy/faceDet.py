import cv2 as cv

color = (0, 255, 255)
grosor = 2

img = cv.imread('imgs/LennaRGB.png')

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

clasificador = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

caras = clasificador.detectMultiScale(gray)

for (x, y, w, h) in caras:
    cv.rectangle(img, (x, y), (x + w, y + h), color, grosor)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()