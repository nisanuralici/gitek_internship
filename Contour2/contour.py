# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:09:06 2023
@author: Nisanur
"""

import cv2
import numpy as np

# orijinal görseli yükleme
image = cv2.imread("paint.png")

# Gri görüntüye çevirme
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenarları tespit etme
edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# Kenarları aşındırma
kernel = np.ones((4, 4), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)

# Konturları bulma
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Kesilmiş nesneleri saklamak için boş bir liste oluştur
cropped_objects = []

# Her bir kontur için sınırlama kutusu çıkart, kesilmiş nesneyi sakla ve kaydet
for idx, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(bounded_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(bounded_image, f"Start: ({x}, {y})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 255), 1)
    cv2.putText(bounded_image, f"End: ({x + w}, {y + h})", (x, y + h + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 255), 1)

    # Kesilmiş nesneyi sakla ve kaydet
    cropped_object = image[y:y + h, x:x + w]
    cropped_objects.append(cropped_object)
    cv2.imshow(f'Cropped Object {idx+1}', cropped_object)
    cv2.imwrite(f'cropped_object_{idx+1}.jpg', cropped_object)  # Görseli kaydet
    cv2.waitKey(0)

# Sınırlama kutuları çizilmiş görüntüyü göster
cv2.imshow('Bounded Boxes Image', bounded_image)
cv2.imwrite(f'bounded.jpg', bounded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
