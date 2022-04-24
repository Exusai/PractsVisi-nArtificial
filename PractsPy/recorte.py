import cv2 as cv

color = (0, 0, 255)
grosor = 4
anchoMin = 100

img = cv.imread("imgs/LennaRGB.png", 1)
imgCopy = img.copy()

cv.imshow("Cuadro", img)

def Region(event, x, y, flags, param):
    global x1, y1, img
    if event == cv.EVENT_LBUTTONDOWN:
        x1, y1 = x,y

    if event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        img = imgCopy.copy()
        cv.rectangle(img, (x1, y1), (x, y), color, grosor)

    elif event == cv.EVENT_LBUTTONUP:
        imgRecorte = imgCopy[y1:y, x1:x]
        cv.imshow("Recorte", imgRecorte)
    
    cv.imshow("Cuadro", img)

cv.setMouseCallback("Cuadro", Region)
cv.waitKey(0)