import cv2

image = cv2.imread("img1.jpg")
inverted_image = cv2.bitwise_not(image)

cv2.imshow("Original Image", image)
cv2.imshow("Inverted Image", inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ters çevrilen görüntüyü kaydet
cv2.imwrite("Inverted_Image.jpg", inverted_image)
