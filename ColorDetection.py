
# Notes for this script
# -RGB: Red Green Blue
# -BGR: Blue Green Red
# -***HSV: Hue and Saturation & Lightness/Brightness (we will be using HSV in this script to represent colors)

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # #returns a frame of video and ret which returns false when camera is off or user
    # clicks off

    width = int(cap.get(3))  # 3 is the width property of camera, so this gets the camera capture width
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # You can access individual pixels with cvtColor()
    # BGR_color = np.array([[[255, 0, 0]]])
    # p[0][0] = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([94, 80, 2]) # HSV color value bounds to display. CV2 functions require numpy arrays
    upper_blue = np.array([126, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # masks are a portion of an image.
    # Only colors in states range will be shown

    result = cv2.bitwise_and(frame, frame, mask=mask)
    # bitwise ints follow p^q. Both must be 1's to be true
    # we pass the same image twice, in  our case src1 & src2 are just our frame. The function will compare the mask
    # to the frame and get rid of pixels not in the mask's range.

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask) # the T/F values from our range

    if cv2.waitKey(1) == ord('q'):
        # waitKey returns the ASCII Value of the key pressed. ord() returns the ASCII val of the desired stop key
        break

cap.release()  # releases camera from script so other programs can use it.
cv2.destroyAllWindows()
