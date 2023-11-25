#importing modules
from ultralytics import YOLO
from pyfirmata import Arduino,SERVO,util
from time import sleep

#giving the particular port id from the ardruino ide
port = 'COM<>'
pin1 = 10  # remeber to connect to digital pin only
pin2 = 11  # 1st servo for horizontol rotation and 2nd servo for vertical rotation 
board=Arduino(port)

#inittializing the servo module
board.digital[pin1].mode=SERVO
board.digital[pin2].mode=SERVO

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
    
    #need to add delays as per or machine learning code 
    sleep(0.15)

###############################################################
                #machine learning code will be put here  
###############################################################
# Load a model
model = YOLO("yolov8n.yaml")
model.train(data="coco128.yaml", epochs=3)  # train the model

while True:
    #input will be taken from the output variable of the machine learning code
    x=input()
    
    # 1 : plastic waste and 2 : non plastic waste
    if x=="1":
        for i in range(0,90):
            rotateServo(pin1,i)
    elif x=="2":
        for i in range(0,180):
            rotateServo(pin1,i)

