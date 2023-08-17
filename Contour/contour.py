import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('moon.jpg')

# Görüntüyü gri tonlamalı yap
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenar tespiti için Canny kenar dedektörünü kullan
edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# Kenar görüntüsünde konturları bul
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Kesilmiş nesneleri saklamak için boş bir liste oluştur
cropped_objects = []

# Her bir kontur için sınırlama kutusu çıkart ve kesilmiş nesneyi sakla
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cropped_object = image[y:y+h, x:x+w]
    cropped_objects.append(cropped_object)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Sınırlama kutuları ve kesilmiş nesneleri içeren görüntüyü göster
cv2.namedWindow('Bounded Boxes and Cropped Objects', cv2.WINDOW_NORMAL)
cv2.imshow('Bounded Boxes and Cropped Objects', image)
cv2.waitKey(0)

# Kesilmiş nesneleri ayrı bir pencerede göster ve kaydet
for idx, cropped_object in enumerate(cropped_objects):
    cv2.imshow(f'Cropped Object {idx+1}', cropped_object)
    cv2.imwrite(f'cropped_object_{idx+1}.jpg', cropped_object)  # Görseli kaydet
    cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
