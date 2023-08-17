# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:40:24 2023

@author: Nisanur
"""

import cv2
import numpy as np
# Read the image
image = cv2.imread('img1.jpg')
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresholded_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Thresholded Image', thresholded_image)
