import cv2 as cv

umbral = 220
color = (0, 0, 0)
grosor = 2
texto = ""
fuente = cv.FONT_HERSHEY_SIMPLEX
escala = .8

# open figure
img = cv.imread("PractsPy/imgs/Figs1.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# binarize
ret, img_bin = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY)

# find contours
contours, hierarchy = cv.findContours(img_bin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# draw contours on img
#cv.drawContours(img, contours, -1, color, grosor)

# drop largest contour (background)
contours.sort(key=cv.contourArea, reverse=True)
contours = contours[1:]

# draw bounding rectangles on img
for cnt in contours:
    x, y, ancho, alto = cv.boundingRect(cnt)
    cv.rectangle(img, (x, y), (x + ancho, y + alto), color, grosor)
    margen_err = 0.01 * cv.arcLength(cnt, True)
    contorno_aprox = cv.approxPolyDP(cnt, margen_err, True)
    cv.drawContours(img, [contorno_aprox], -1, color, grosor)

    if len(contorno_aprox) == 6:
        texto = "hexagono"
    elif len(contorno_aprox) == 5:
        texto = "pentagono"
    elif len(contorno_aprox) == 4:
        texto = "cuadrado"
    elif len(contorno_aprox) == 3:
        texto = "triangulo"
    elif len(contorno_aprox) == 2:
        texto = "linea"
    else:
        texto = "otro"

    (ancho_texto, alto_texto)  = cv.getTextSize(texto, fuente, escala, grosor)[0]
    pos_x = int(x + (ancho-ancho_texto)/2)
    pos_y = int(y + (alto+alto_texto)/2)

    # display text
    cv.putText(img, texto, (pos_x, pos_y), fuente, escala, color, grosor)
    

# display image
cv.imshow("Figuras", img)
#cv.imshow("Binarizada", img_bin)
cv.waitKey(0)
cv.destroyAllWindows()