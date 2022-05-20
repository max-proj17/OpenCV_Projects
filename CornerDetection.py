# --------------------------------------------------------------------
# ----OpenCV uses J.Shi and C.Tomasi's modication of the Harris Corner detector
# ----called "Good Features to Track". Documentation here:
# ----https://docs.opencv.org/3.4/d4/d8c/tutorial_py_shi_tomasi.html
# --------------------------------------------------------------------

# ---------------------------------------------------------------------
# -----This script displays detected corners as blue circles and draws
# -----lines from every point excluding itself. This forms a "graph"
# -----that is symmetric, transitive and not reflexive

import numpy as np
import cv2

image = cv2.imread('proj_files/Old _anua_ Drawing.jpg')
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# we are detecting corners on gray_image then drawing the circles on the colored image

corners = cv2.goodFeaturesToTrack(gray, 100, .01, 10);
# In our case we are using params (src_image, num_corners, min_quality, min_Euclidean_Distance)

# min_Euclidean_Distance: is found using the Pythagorean Theorem, to find the distance between two corners.
# The hypotenuse assists the algorithm in deciding whether to include the corner in its detection based
# on the chosen distance

# min_quality: is simply a degree of confidence that the algorithm uses to detect/ignore a corner

# Now we must convert "corners" (which are floats) into integers. In order to draw corners they must be integers.
# We will draw circles where corners are detected

corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()   # this will flatten the array (removes all interior arrays) [[x, y]] -> [x, y]
    cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

for p in range(len(corners)):
    for k in range(p+1, len(corners)): # This loop will draw a line to every corner except for itself.
        corner_1 = tuple(corners[p][0])   # Again this "graph" will be symmetric, transitive and not reflexive
        corner_2 = tuple(corners[k][0])
        color = tuple(map(lambda x: int(x),np.random.randint(0, 255, size=3)))
        # Note: numpy 64 or 32-bit integers are different from Python integers
        # the map function takes each val in the iterable and returns the result
        # lambda x: int(x) is converting our numpy ints to python ints. You can have any defined
        # function in the 1st map parameter Ex: def add_three(n): return n+n+n, map(add_three, iterable)
        cv2.line(image, corner_1, corner_2, color, 1)
cv2.imshow('Frame', image)

cv2.waitKey(0)

cv2.destroyAllWindows()