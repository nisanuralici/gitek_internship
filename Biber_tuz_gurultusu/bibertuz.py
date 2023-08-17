import cv2
import numpy as np

img = cv2.imread('img1.jpg', 0)
salt_pepper_prob = 0.02  # Beyaz ve siyah nokta oranı
random_matrix = np.random.rand(*img.shape)
img[random_matrix < salt_pepper_prob / 2] = 0  # Siyah noktalar
img[random_matrix > 1 - salt_pepper_prob / 2] = 255  # Beyaz noktalar

# Median Blur filtresi
ksize = 5
median_blur_result = cv2.medianBlur(img, ksize)

cv2.imshow('Noisy Image', img)
cv2.imshow('Median Blur Result', median_blur_result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Tuz-biber gürültülü ve Median Blur uygulanmış görüntüyü kaydet
cv2.imwrite("Median_Blur_Result_with_Noise.jpg", img)
