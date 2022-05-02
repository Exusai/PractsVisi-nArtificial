import cv2 as cv

umbral = 100
color = (0, 0, 255)
grosor = 2
texto = ""
fuente = cv.FONT_HERSHEY_SIMPLEX
escala = .8
similitud = 0.5

imgOrg = cv.imread("PractsPy/imgs/2s.png")
img = cv.cvtColor(imgOrg, cv.COLOR_BGR2GRAY)


img1 = cv.imread("PractsPy/imgs/1.png", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("PractsPy/imgs/2.png", cv.IMREAD_GRAYSCALE)
img3 = cv.imread("PractsPy/imgs/3.png", cv.IMREAD_GRAYSCALE)

# binarize imag1, img2, img3
ret, img1_bin = cv.threshold(img1, umbral, 255, cv.THRESH_BINARY_INV)
ret, img2_bin = cv.threshold(img2, umbral, 255, cv.THRESH_BINARY_INV)
ret, img3_bin = cv.threshold(img3, umbral, 255, cv.THRESH_BINARY_INV)

# find contours
contours1, hierarchy1 = cv.findContours(img1_bin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv.findContours(img2_bin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours3, hierarchy3 = cv.findContours(img3_bin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

contour1 = contours1[0]
contour2 = contours2[0]
contour3 = contours3[0]

# binarize img
ret, img_bin = cv.threshold(img, umbral, 255, cv.THRESH_BINARY_INV)

# find contours
contours, hierarchy = cv.findContours(img_bin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


for contorno in contours:
    x, y, ancho, alto = cv.boundingRect(contorno)
    if cv.matchShapes(contorno, contour1, cv.CONTOURS_MATCH_I1, 0.0) < similitud:
        cv.drawContours(imgOrg, [contorno], -1, color, grosor)
        texto = "1"
    elif cv.matchShapes(contorno, contour2, cv.CONTOURS_MATCH_I1, 0.0) < similitud:
        cv.drawContours(imgOrg, [contorno], -1, color, grosor)
        texto = "2"
    elif cv.matchShapes(contorno, contour3, cv.CONTOURS_MATCH_I1, 0.0) < similitud:
        cv.drawContours(imgOrg, [contorno], -1, color, grosor)
        texto = "3"
    else:
        cv.drawContours(imgOrg, [contorno], -1, color, grosor)
        texto = "otro"

    (ancho_texto, alto_texto)  = cv.getTextSize(texto, fuente, escala, grosor)[0]
    pos_x = int(x + (ancho-ancho_texto)/2)
    pos_y = int(y + (alto+alto_texto)/2)

    print("Detección: ", texto)
    print("Similutud: ", cv.matchShapes(contorno, contour3, cv.CONTOURS_MATCH_I1, 0.0))
    print("*********************************************************")

    # display text
    cv.putText(imgOrg, texto, (pos_x, pos_y), fuente, escala, [0, 255, 0], grosor)

# show image
cv.imshow("img", imgOrg)
cv.waitKey(0)
cv.destroyAllWindows()

