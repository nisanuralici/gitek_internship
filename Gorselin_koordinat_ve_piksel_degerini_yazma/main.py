import cv2

def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global img
        img = img_original.copy()  # Önceki yazıları temizle
        pixel_value = img[y, x]
        cv2.putText(img, f'Coordinates: ({x}, {y})', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f'Pixel Value: {pixel_value}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('image', img)

        global saved_image
        saved_image = img.copy()  # Görüntüyü kaydetmek için kopyala

img_original = cv2.imread('img1.jpg', 0)
img = img_original.copy()  # İlk görüntü kopyasını al
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('w'):
        break
    elif key == ord('s'):
        cv2.imwrite('saved_image.jpg', saved_image)
        print("Görüntü kaydedildi: saved_image.jpg")

cv2.destroyAllWindows()
