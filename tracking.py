import cv2
import numpy as np

image_path = r'proj_files/trackimage.jpg'

image = cv2.imread(image_path, 0) # 0 is to import as grayscale
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
template = cv2.imread('proj_files/foot from image.jpg', 0)
template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)

h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# documentation suggests testing all methods for object detection to see which one
# works best for our problem

for method in methods:
    image2 = image.copy()
    # we copy to image, so it "clears" the previous rectangle before testing the next method
    result = cv2.matchTemplate(image2, template, method)
    # this uses the sliding window method: result is the output array that shows successful matches.
    # Ex: A 4x4 image with a template of 2x2 would have a result array of 3x3 with 1's and 0's
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # minMaxLoc will give us the values to the left, but we only care about min_loc & max_loc (indexes)
    # because we want to reverse engineer the location of the match to draw a rectangle
    # locations are tuples of (int, int)
    # print(min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: # these methods take in the min_loc. Other methods use max_loc
        location = min_loc
    else:
        location = max_loc

    right_bottom = (location[0] + w,location[1] + h)
    cv2.rectangle(image2, location, right_bottom, 0, 5)
    #####################
    # location________
    # |              |
    # |              |
    # ---------------right_bottom
    #####################
    # location gives us width, right_bottom gives us height
    cv2.imshow('Found', image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



