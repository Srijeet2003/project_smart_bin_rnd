#!/usr/bin/env python
# coding: utf-8

from ultralytics import YOLO
model=YOLO('last (6).pt')

import cv2
import math
import matplotlib.pyplot as plt

from pyfirmata import Arduino,SERVO,util
from time import sleep
port = '/dev/ttyACM0'
pin1 = 10
pin2 = 11
board = Arduino(port)
board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO
def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)

cap = cv2.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 720)

classNames=["non-plastic","plastic"]

while True:
    ret, img= cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes

    for box in boxes:
    # bounding box
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

    # put box in cams
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

    # confidence
    confidence = math.ceil((box.conf[0]*100))/100
    print("Confidence =",confidence)

    # class name
    cls = int(box.cls[0])
    print("Class name =", classNames[cls])

    # object details
    org = [x1, y1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2

    cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
    
    if classNames=="plastic":
        for i in range(0,90,0.5):
            rotateservo(pin1,i)
            print("90 degree")
        break

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cap.release()
cv2.destroyAllWindows()