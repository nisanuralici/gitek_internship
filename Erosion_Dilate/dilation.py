import  cv2
import numpy as np

img = cv2.imread("star.jpg", 0)
kernel = np.ones((4,4),np.uint8)
dilation_result = cv2.dilate(img,kernel,iterations=1)
cv2.namedWindow("original image",cv2.WINDOW_NORMAL)
cv2.imshow("original image",img)
cv2.namedWindow("dilation result",cv2.WINDOW_NORMAL)
cv2.imshow("dilation result", dilation_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
