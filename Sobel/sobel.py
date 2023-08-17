import cv2
import numpy as np

img = cv2.imread('img1.jpg', 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)
cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
cv2.namedWindow("Sobel X",cv2.WINDOW_NORMAL)
cv2.imshow('Sobel X', sobelx)
cv2.namedWindow("Sobel Y",cv2.WINDOW_NORMAL)
cv2.imshow('Sobel Y', sobely)
cv2.namedWindow("Sobel XY",cv2.WINDOW_NORMAL)
cv2.imshow('Sobel XY', sobelxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
