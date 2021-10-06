import cv2
import numpy as np

###########
import utilis

webcam = False
path = '1.jpg' #card size is 85*54 in mm
cap = cv2.VideoCapture(0)
cap.set(10,160) #10 is id for brightness
cap.set(3, 1920) # 3 is id for width
cap.set(4, 1080) # 4 is id for height

while True:
    if webcam: success, img = cap.read()
    else: img = cv2.imread(path)
    img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    img = cv2.resize(img,(540,360))
    img, conts = utilis.contours(img,showCanny=False, draw = True, minArea=5000,filter = 4)

    if len(conts) !=0:
        biggest = conts[0][2]
        print(biggest)

    cv2.imshow('original', img)
    cv2.waitKey(0)