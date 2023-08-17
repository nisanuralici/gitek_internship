import numpy as np
import cv2

width = 800
height = 600
empty_image = np.zeros((height, width, 3), dtype=np.uint8)
cv2.imshow("Empty Image", empty_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Empty_Image.jpg", empty_image)
