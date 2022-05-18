import cv2
import random;
image_path = r'Old _anua_ Drawing.jpg'

image = cv2.imread(image_path)

##for i in range(100):
  ##  for j in range(image.shape[1]):
    ##    image[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#will make a copy box with height/width specified
tag = image[500:700, 600:900]
image[100:300, 650:950] = tag

cv2.imshow('Sample Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
