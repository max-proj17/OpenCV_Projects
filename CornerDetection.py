# --------------------------------------------------------------------
# ----OpenCV uses J.Shi and C.Tomasi's modication of the Harris Corner detector
# ----called "Good Features to Track". Documentation here:
# ----https://docs.opencv.org/3.4/d4/d8c/tutorial_py_shi_tomasi.html
# --------------------------------------------------------------------

import numpy as np
import cv2

image = cv2.imread('proj_files/Old _anua_ Drawing.jpg')