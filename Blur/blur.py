import cv2

img = cv2.imread("img1.jpg", 1)
ksize = (5, 5)
blur_result = cv2.GaussianBlur(img, ksize, sigmaX=0)

cv2.imshow("Original image", img)
cv2.imshow("Blur result", blur_result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Bulanıklaştırılmış görüntüyü kaydet
cv2.imwrite("Blur_Result.jpg", blur_result)
