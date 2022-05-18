import cv2
import numpy as np

##you can download a video, put it in the project folder and then replace the 0 with the file name

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # #returns a frame of video and ret which returns false when camera is off or user
    # clicks off

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):  # waitKey returns the ASCII Value of the key pressed. ord() returns the ASCII val of the desired stop key
        break

cap.release()  # releases camera from script so other programs can use it.
cv2.destroyAllWindows()