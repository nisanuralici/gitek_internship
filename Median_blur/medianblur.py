import cv2

img = cv2.imread("img1.jpg", 1)
ksize = 5
median_blur_result = cv2.medianBlur(img, ksize)

cv2.imshow("Original image", img)
cv2.imshow("Median blur result", median_blur_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Median Blur işlemi sonucunu kaydet
cv2.imwrite("Median_Blur_Result.jpg", median_blur_result)
