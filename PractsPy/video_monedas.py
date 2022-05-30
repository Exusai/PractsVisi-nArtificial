import cv2 as cv
import numpy as np

fps = 30
velocidad_reproduccion = int(1000/fps)

video = cv.VideoCapture('imgs/monedas.mp4')

if not video.isOpened():
    print('No se pudo abrir el video')
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print('No se pudo leer el video')
        break

    # scale down video 
    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    cv.imshow('Monedas', frame)

    if cv.waitKey(velocidad_reproduccion) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()