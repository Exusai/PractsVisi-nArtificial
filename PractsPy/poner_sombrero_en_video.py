import cv2 as cv
import numpy as np

fps = 30
velocidad_reproduccion = int(1000/fps)

sombrero = cv.imread('imgs/Sombrero.png')

talla_sombrero = 1.2

ancho_sombrero, alto_sombrero = sombrero.shape[:2]
#ancho_img, alto_img = img.shape[:2]


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
        #cv.rectangle(frame, (x, y), (x + w, y + h), color, grosor)
        try:
            sombrero_resized = cv.resize(sombrero, (w, h))

            sombrero_gray = cv.cvtColor(sombrero, cv.COLOR_BGR2GRAY)
            th, threshed = cv.threshold(sombrero_gray, 2, 255, cv.THRESH_BINARY_INV)

            #cv.imshow('Sombrero', threshed)

            # offset sombrero by face height
            offset_x = x + (w - sombrero_resized.shape[1]) // 2
            offset_y = y - sombrero_resized.shape[0] - 10
            frame[offset_y:offset_y + sombrero_resized.shape[0], offset_x:offset_x + sombrero_resized.shape[1]] = np.bitwise_and(frame[offset_y:offset_y + sombrero_resized.shape[0], offset_x:offset_x + sombrero_resized.shape[1]], sombrero_resized)

        except:
            pass

    cv.imshow('Camara web', frame)

    if cv.waitKey(velocidad_reproduccion) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()