import cv2 as cv
import numpy as np

fps = 30
velocidad_reproduccion = int(1000/fps)


color = (0, 255, 255)
grosor = 2
clasificador = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

incremento_brillo = 0

def increase_brightness(valor):
    global incremento_brillo
    incremento_brillo = valor

def modificar_brillo(img):
    global incremento_brillo
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)
    lim = 255 - incremento_brillo
    v[v > lim] = lim                
    v[v<=lim] += incremento_brillo  # si se comenta este el brillo solo disminuye

    hsv = cv.merge((h, s, v))
    #v += incremento_brillo
    #v = np.clip(v, 0, 255)
    hsv = cv.merge((h, s, v))
    return cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

cv.namedWindow('Camara web')
cv.createTrackbar('Brillo', 'Camara web', 0, 255, increase_brightness)


video = cv.VideoCapture('imgs/faces.mp4')

if not video.isOpened():
    print('No se pudo abrir el video')
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print('No se pudo leer el video')
        break

    # scale down video 
    frame = cv.resize(frame, (0, 0), fx=1, fy=1)

    frame = modificar_brillo(frame)

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detectar rostros
    rostros = clasificador.detectMultiScale(frame_gray, 1.3, 5)
    for x, y, w, h in rostros:
        cv.rectangle(frame, (x, y), (x + w, y + h), color, grosor)
    

    cv.imshow('Camara web', frame)

    if cv.waitKey(velocidad_reproduccion) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()