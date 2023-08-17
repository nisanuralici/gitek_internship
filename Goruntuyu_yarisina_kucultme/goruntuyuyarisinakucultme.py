import cv2

image = cv2.imread("img1.jpg")
height, width = image.shape[:2]

new_height = int(height / 2)
new_width = int(width / 2)
resized_image = cv2.resize(image, (new_width, new_height))

cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Yeniden boyutlandırılmış görüntüyü kaydet
cv2.imwrite("Resized_Image.jpg", resized_image)
