import cv2 as cv
import os
import numpy as np

imgs_path = 'imgs_recon/'
images_in_folder = os.listdir(imgs_path)

tr = 100
blur_size = (5, 5)

image = 0

measuring = False

parameters = cv.aruco.DetectorParameters_create()
aruci_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_5X5_50)

def new_tr(x):
    global tr
    tr = x
    return tr

def new_img(x):
    global image
    image = int(x)
    return image

def toogle_measuring(x):
    global measuring
    measuring = not measuring
    return measuring

lower_hue = 20 # aprox 70° de 360°
lower_saturation = 70 # aprox 30%
lower_value = 25 # or luminance, aprox 10%

upper_hue = 200 # aprox 150° de 360°
upper_saturation = 255 # 100%
upper_value = 255 # or luminance, aprox 60%

hsv_upper = (upper_hue, upper_saturation, upper_value)
hsv_lower = (lower_hue, lower_saturation, lower_value)

def black_object_contour_det(img):
    image_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    image_gray = cv.blur(image_gray, blur_size)

    # segmentate image based on trackbar value
    image_gray = cv.threshold(image_gray, tr, 255, cv.THRESH_BINARY)[1]

    # find contours
    contours, _ = cv.findContours(image_gray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    return contours

def green_object_contour_det(img):
    image_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    image_hsv = cv.medianBlur(image_hsv, 5)

    # segmentate
    image_hsv = cv.inRange(image_hsv, hsv_lower, hsv_upper)

    # find contours
    contours, _ = cv.findContours(image_hsv, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    return contours

# create window
cv.namedWindow('img', cv.WINDOW_NORMAL)
cv.resizeWindow('img', 600, 700)

# create trackbar
#cv.createTrackbar('tr', 'img', 0, 255, lambda x: new_tr(x))
cv.createTrackbar('Image', 'img', 0, len(images_in_folder)-1, lambda x: new_img(x))
cv.createTrackbar('Measuring', 'img', 0, 1, lambda x: toogle_measuring(x))

while True:
    talones = 0
    baras = 0

    image = cv.imread(imgs_path + images_in_folder[int(cv.getTrackbarPos('Image', 'img'))])
    
    # resieze image to 1/4 size
    image = cv.resize(image, None, fx=0.3, fy=0.3)

    # rotate image by 90°
    image = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)

    black_object_contours = black_object_contour_det(image)
    green_object_contours = green_object_contour_det(image)

    # discard contours that are too small or too large
    black_object_contours = [c for c in black_object_contours if cv.contourArea(c) > 100 and cv.contourArea(c) < 10000]
    green_object_contours = [c for c in green_object_contours if cv.contourArea(c) > 100 and cv.contourArea(c) < 5000]

    # concatenate contours
    contours = black_object_contours + green_object_contours

    if measuring:
        corners, _, _ = cv.aruco.detectMarkers(image, aruci_dict, parameters=parameters)

        if len(corners) > 0:
            # draw markers
            image = cv.aruco.drawDetectedMarkers(image, corners)
            aruco_perimeter = cv.arcLength(corners[0], True)

            # get aruco min and max x and y
            aruco_min_x = corners[0][0][0][0]
            aruco_min_y = corners[0][0][0][1]
            aruco_max_x = corners[0][0][0][0]
            aruco_max_y = corners[0][0][0][1]
            
            # pixel to meter conversion
            pixel_cm_ratio = aruco_perimeter / 20

            # list of centers of contours
            centers = []
            for c in contours:
                [x, y, w, h] = cv.boundingRect(c)
                centers.append((x + w/2, y + h/2))

            # check if centers are inside aruco perimeter
            index_to_drop = []
            i = 0
            for c in centers:
                if (cv.pointPolygonTest(corners[0], c, True) >= 0):
                    index_to_drop.append(i)
                i += 1

            # drop contours that are inside aruco perimeter
            contours = [c for i, c in enumerate(contours) if i not in index_to_drop]
            
            for c in contours:
                rect = cv.minAreaRect(c)
                (x,y), (w,h), angle = rect
                box = cv.boxPoints(rect)
                box = np.int0(box)

                object_width = w/pixel_cm_ratio
                object_height = h/pixel_cm_ratio   

                object_width = round(object_width, 2)
                object_height = round(object_height, 2)

                cv.circle(image, (int(x), int(y)), 5, (255, 0, 0), -1)
                cv.polylines(image, [box], True, (0, 255, 0), 2)
                cv.putText(image, str(object_width) + 'X' + str(object_height), (int(x), int(y)), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1)
        
    else:
        for green_contour in green_object_contours:
            # get rectangle bounding contour
            [x, y, w, h] = cv.boundingRect(green_contour)

            # label contour as "bara"
            cv.putText(image, "talon", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 1)
            talones += 1

            # plot contour
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        for black_contour in black_object_contours:
            # get rectangle bounding contour
            [x, y, w, h] = cv.boundingRect(black_contour)

            # label contour as "talón"
            cv.putText(image, "bara", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 1)
            baras += 1

            # plot contour
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

        # display number of talones and baras
        cv.putText(image, "Talones: " + str(talones), (10, 20), cv.FONT_HERSHEY_SIMPLEX, .8, (0, 0, 0), 2)
        cv.putText(image, "Baras: " + str(baras), (10, 45), cv.FONT_HERSHEY_SIMPLEX, .8, (0, 0, 0), 2)

    cv.imshow('img', image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.waitKey(0)
cv.destroyAllWindows()