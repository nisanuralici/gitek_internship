import cv2

img = cv2.imread("img.jpg", 1)  # Renkli olarak görüntüyü yükle

x = 150
y = 150
pixel_value = img[y, x]

# Piksel değerini görüntünün üzerine yazdır
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)  # Beyaz renk
thickness = 2

text = f"Piksel ({x}, {y}): Deger={pixel_value}"
text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
text_x = max(x - text_size[0] // 2, 0)  # Yazının görüntü sınırlarından taşmaması için x koordinatı hesaplanır
text_y = max(y + text_size[1] // 2, text_size[1])  # Yazının görüntü sınırlarından taşmaması için y koordinatı hesaplanır

cv2.putText(img, text, (text_x, text_y), font, font_scale, font_color, thickness)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
