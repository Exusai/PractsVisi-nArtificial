import cv2 as cv

color = (0, 255, 255)
grosor = 2

img = cv.imread('imgs/LennaRGB.png')

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

clasificador = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
clasificadorOjos = cv.CascadeClassifier('haarcascade_eye.xml')

caras = clasificador.detectMultiScale(gray)

for (x, y, w, h) in caras:
    cv.rectangle(img, (x, y), (x + w, y + h), color, grosor)
    cara = gray[y:y + h, x:x + w]
    ojos = clasificadorOjos.detectMultiScale(cara, 1.3, 5)
    for (x1, y1, w1, h1) in ojos:
        radio = int((h1+w1) / 4)
        cv.circle(img, (x1 + x + radio, y1 + y + radio), radio, (0, 0, 255), grosor)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()