import cv2
import numpy as np

##you can download a video, put it in the project folder and then replace the 0 with the file name

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # #returns a frame of video and ret which returns false when camera is off or user
    # clicks off

    width = int(cap.get(3))  # 3 is the width property of camera, so this gets the camera capture width
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)  # unsigned integer 8 bits
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)  ##put smaller image in top left hand corner
    image[height // 2:, :width // 2] = smaller_frame  ##put image bottom left
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)  ##top right
    image[height // 2:, width // 2:] = smaller_frame  ##bottom right
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):  # waitKey returns the ASCII Value of the key pressed. ord() returns the ASCII val of the desired stop key
        break

cap.release()  # releases camera from script so other programs can use it.
cv2.destroyAllWindows()
