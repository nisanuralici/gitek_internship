import  cv2
import numpy as np

img = cv2.imread("star.jpg", 0)
kernel = np.ones((4,4),np.uint8)
erosion_result = cv2.erode(img,kernel,iterations=1)
cv2.namedWindow("original image",cv2.WINDOW_NORMAL)
cv2.imshow("original image",img)
cv2.namedWindow("erosion ressult",cv2.WINDOW_NORMAL)
cv2.imshow("erosion ressult", erosion_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
