import cv2
import numpy as np

img = cv2.imread("img1.jpg", 1)
edges = cv2.Canny(img, 100, 200)
cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)
cv2.namedWindow("Canny",cv2.WINDOW_NORMAL)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
