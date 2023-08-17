import cv2

img = cv2.imread("img1.jpg", 1)
ksize = (5, 5)
sigma_x = 0
gaussian_blur_result = cv2.GaussianBlur(img, ksize, sigmaX=sigma_x)

cv2.imshow("Original image", img)
cv2.imshow("Gaussian blur result", gaussian_blur_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian bulanıklaştırma sonucunu kaydet
cv2.imwrite("Gaussian_Blur_Result.jpg", gaussian_blur_result)
