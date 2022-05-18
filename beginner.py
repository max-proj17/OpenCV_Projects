import cv2

image_path = r'Old _anua_ Drawing.jpg'

image = cv2.imread(image_path)

cv2.imshow('Sample Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
