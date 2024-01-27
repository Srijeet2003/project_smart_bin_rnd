#importing modules
from ultralytics import YOLO
from pyfirmata import Arduino,SERVO,util
from pymata4 import pymata4
from time import sleep
import time
import os
import cv2

#giving the particular port id from the ardruino ide
port = '/dev/ttyACM0'
pin1 = 10  # remeber to connect to digital pin only
# pin2 = 11  # 1st servo for horizontol rotation and 2nd servo for vertical rotation 
trig_pin = 12
echo_pin = 13
board=Arduino(port)
board1=pymata4.Pymata4()

#inittializing the servo module
board.digital[pin1].mode=SERVO
# board.digital[pin2].mode=SERVO

def rotateServo(pin,angle):
    board.digital[pin].write(angle) 
    #need to add delays as per or machine learning code 
    sleep(0.15)
    
def servoCallback(data):
    print("the level of garbage in bin is at height: ",data[2])
    if data[2]<100:
        print("the bin is full , please empty it")
        
board1.set_pin_mode_sonar(trig_pin,echo_pin,servoCallback)

###############################################################
                #machine learning code will be put here  
###############################################################
# # Load a model
# model=YOLO("yolov8n.yaml")
# model.train(data="coco128.yaml", epochs=3)  # train the model
# # take a live camera feed
# cap=cv2.VideoCapture("<camera node address>")
# ret, frame = cap.read()
# H, W, _ = frame.shape
# out=cv2.VideoWriter("<camera path>",cv2.VideoWriter_fourcc(*'MP4V'),int(cap.get(cv2.CAP_PROP_FPS)),(W, H))
# # get some kind of True or false op 
# threshold=0.5

# while ret:
#     results=model(frame)[0]
#     for result in results.boxes.data.tolist():
#         x1,y1,x2,y2,score,class_id=result

#         if score>threshold:
#             cv2.rectangle(frame,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),4)
#             cv2.putText(frame,results.names[int(class_id)].upper(),(int(x1),int(y1-10)),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1.3,(0,255,0),3,cv2.LINE_AA)

#     out.write(frame)
#     ret,frame=cap.read()

# cap.release()
# out.release()
# cv2.destroyAllWindows()

while True:
    #input will be taken from the output variable of the machine learning code
    x=input("enter the choice:")
    
    # 1 : plastic waste and 2 : non plastic waste
    if x=="1":
        for i in range(0,90):
            rotateServo(pin1,i)
            # rotateServo(pin2,90) #to drop the garbage
    elif x=="2":
        for i in range(0,180):
            rotateServo(pin1,i)
            # rotateServo(pin2,90) #to drop the garbage
            
    elif x=="3":
        try:
            time.sleep(0.1)
            board1.sonar_read(trig_pin)
        except:
            board1.shutdown()
            