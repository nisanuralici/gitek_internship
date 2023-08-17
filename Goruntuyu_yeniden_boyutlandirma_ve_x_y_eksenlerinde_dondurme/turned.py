import cv2
img = cv2.imread("img.jpg")
cv2.imshow("orijinal img", img)
cv2.waitKey(0)
 
turned_x = cv2.flip(img, 0)
cv2.imshow("turned_x",turned_x)
cv2.waitKey(0)
turned_y = cv2.flip(img, 1)
cv2.imshow("turned_y",turned_y)
cv2.waitKey(0)

sizes = [(227, 227), (300, 300), (480, 480)]
for width, height in sizes:
    resized_img = cv2.resize(img, (width, height))
    cv2.imshow("resized_goruntu", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

