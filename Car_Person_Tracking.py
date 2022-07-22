import cv2

############################
## The classifier used in this project I retrieved
## from Ratan Singh Dharra's website at https://rsdharra.com/blog/lesson/26.html
############################

# Download car image
file = 'proj_files/Cars-on-highway.jpg'
video = cv2.VideoCapture('proj_files/CarsTrim.mp4')
# Classifier that is pre-trained
classifier_file = 'proj_files/cars.xml'
# Create the classifier using Haar Cascades
tracker = cv2.CascadeClassifier(classifier_file)

#runs until video "ends"

while True:
    # Read the current frame
    (read, frame) = video.read()

    # Safe check if video read was successful
    if read:
        # turn image to grayscale for the haar cascades
        bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    # Detect cars. Will detect coordinates (as a square of the window) of where the classifiers think a car is
    # ex: [375, 262, 348, 348] = [top left coordinate(x), top left coordinate(y), Length of rec, width of rect]
    cars = tracker.detectMultiScale(bw)

    # Draw the squares
    for (x, y, w, h) in cars:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display bw frame
    cv2.imshow('Car Detector', frame)

    cv2.waitKey(1)





