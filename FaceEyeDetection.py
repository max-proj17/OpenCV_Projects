import cv2
import numpy as np

###############################
# This facial detection program uses Haar Cascade Detection.
# It is one of the oldest yet powerful face detection algorithms to be invented.
# It is a machine-learning based approach but was famous before deep-learning was.
#
# Cascade functions are trained with positive/negative views of an object and can
# then detect the object in question. Once a Cascade function produces an output, it is used as input for the next
# iteration of the function until it can accurately detect the object a majority of the time.
#
# Haar- features include edge, line and center-surround features. These symbolize things like the distance between eyes.
# Cascade Classifiers don't apply every "feature" from the images the function was trained on.
# Instead, features are grouped in stages. If a section of the image fails the first stage we discard it.
# If it passes we move on to the second stage and only indentify it as a face region when all stages pass.
# Deep learning has replaced Haar Features with Cascade Classifiers due to its superior accuracy and speed.
#
# Read more about Haar-cascade detection here: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
################################


# The classifiers used here are pre-trained and come with OpenCV

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# CascadeClassifier(Path where classifiers are stored on our computer + the specific classifier we want)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # grayscale image of our frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # detectMultiScale will return the positions of the faces in the image
    # detectMultiScale(image, scale factor, minNeighbors)
    # scale factor: shrinks input image. Lower increases accuracy & decreases speed. Higher does the opposite.
    # minNeighbors: determines how many rectangles to detect to mark it as a face. Essentially an accuracy scalar.

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 5)
        reg_oi = gray[y:y+w, x:x+w]
        # here we are extracting the face from the grayscale image based on coordinates from the face detector
        reg_oi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(reg_oi, 1.3, 5)
        #Now we detect the eyes in each face
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(reg_oi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()