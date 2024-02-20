from ultralytics import YOLO
import cv2
import math
import matplotlib.pyplot as plt
from pyfirmata import Arduino, SERVO, util
from time import sleep

# Initialize Arduino board and servo pins
port = '/dev/ttyACM0'
pin1 = 10
pin2 = 11
board = Arduino(port)
board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO

# Function to rotate servo motor
def rotateservo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.05)  # Adjust the sleep duration to control the speed of the servo

# Load YOLO model
model = YOLO('last (6).pt')

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set frame width
cap.set(4, 480)  # Set frame height

# Define class names
classNames = ["non-plastic", "plastic"]

# Variable to track if plastic is detected
plastic_detected = False
non_plastic_detected = False

try:
    while True:
        # Read frame from webcam
        ret, img = cap.read()

        # Perform object detection using YOLO
        results = model(img, stream=True)

        for r in results:
            boxes = r.boxes

        for box in boxes:
            # Get box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Get confidence and class name
            confidence = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            # Display confidence and class name
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

            # If object is plastic, rotate servo motor
            if classNames[cls] == "plastic":
                for i in range(45, 90, 5):  # Adjust the range and increment to limit the movement
                    rotateservo(pin1, i)
                    print("Rotating servo")
                plastic_detected = True

            elif classNames[cls] == "non-plastic":
                # Handle non-plastic detection here
                # For example, you can rotate another servo connected to pin2
                for i in range(135, 90, -5):  # Adjust the range and increment to limit the movement
                    rotateservo(pin1, i)
                    print("Rotating another servo")
                non_plastic_detected = True
                
        # If plastic is detected, stop the servo
        if plastic_detected:
            board.digital[pin1].write(90)  # Set the servo to its default position
            plastic_detected = False  # Reset the flag
            
        if non_plastic_detected:
            board.digital[pin1].write(90)  # Set the other servo to its default position
            non_plastic_detected = False  # Reset the flag

        # Display frame
        cv2.imshow('Webcam', img)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

finally:
    # Stop servo and release webcam when the program is terminated
    board.digital[pin1].write(90)
    cap.release()
    cv2.destroyAllWindows()