import cv2
import numpy as np
import random;

image_path = r'proj_files/Old _anua_ Drawing.jpg'

image = cv2.imread(image_path)

##image.resize(img, (0,0),fx=0.5, fy=2)       //first param can change dimensions directly, fx, fy chnage size via scalars
##img = cv2.resize(img, cv2.cv2.ROTATE_90_CLOCKWISE)
## cv2.imwrite('new_img.jpg', img)           //downloads the altered image

##for i in range(100):         ##look through first 100 rows
##  for j in range(image.shape[1]):       ##image.shape[1] is the width of the image
##    image[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# will make a copy box with height/width specified

## OpenCV list color vals as Blue, Green then Red

##print(image[0])    //prints first row of image

tag = image[500:700, 600:900] ##take part of an image
image[100:300, 650:950] = tag  ##set random location on image to the image fragment
cv2.imshow('Sample Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


