import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # #returns a frame of video and ret which returns false when camera is off or user
    # clicks off

    width = int(cap.get(3))  # 3 is the width property of camera, so this gets the camera capture width
    height = int(cap.get(4))

    image = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    # The statement above draws line on frame. Parameters are frame, coordinates of the line, color & thickness
    image = cv2.line(image, (0, height), (width, 0), (0, 255, 0), 10)
    image = cv2.rectangle(image, (100, 100), (200, 200), (128, 128, 128), 5)
    # parameters for the statement above are image source, center position, radius, color and thickness respectively
    image = cv2.circle(image, (300, 300), 60, (0, 0, 255), -1)
    # image source, center pos, radius, color, line thickness or -1 to fill circle

    # Drawing Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image, 'Max is tired!', (10, height-10), font, 2, (0, 0, 0), 5,  cv2.LINE_AA)
    # image source, position, font, font scale, color, line thickness, line type. (LINE_AA renders the text better)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        # waitKey returns the ASCII Value of the key pressed. ord() returns the ASCII val of the desired stop key
        break

cap.release()  # releases camera from script so other programs can use it.
cv2.destroyAllWindows()
