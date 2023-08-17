import cv2

img = cv2.imread("img.jpg")
font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.imshow("image",img)
#text = "Nisanur Alici"
#org = (50, 50)
#fontScale = 1
#color = (255, 0, 0)
#thickness = 2
img = cv2.putText(img, "Nisanur Alici", (50,50), font, 1, (255,0,0), 2)
img = cv2.putText(img, "1031010622", (50,100), font, 1, (255,255,255), 2)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
