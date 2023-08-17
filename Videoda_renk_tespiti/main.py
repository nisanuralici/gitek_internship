import cv2
import numpy as np

# Videoyu açın
cap = cv2.VideoCapture('video.mp4')
# Video kaydetme işlemi için yapılandırma
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Görüntüyü HSV'ye çevirme
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    # Renk aralığını tanımlama
    lower_value = np.array([90, 50, 50])
    upper_value = np.array([130, 255, 255])
    # Maskeleme işlemi
    mask = cv2.inRange(hsv_frame, lower_value, upper_value)
    # Maskelemeli sonuç görüntüsünü oluşturma
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # Sonuçları gösterme
    cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
    cv2.imshow("Original", frame)
    cv2.namedWindow("Mask",cv2.WINDOW_NORMAL)
    cv2.imshow("Mask", mask)
    cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
    cv2.imshow("Result", result) 
    # Sonuçları video dosyasına yazma
    out.write(result)   
    # 'w' tuşuna basıldığında döngüyü kırın
    if cv2.waitKey(10) & 0xFF == ord('w'):
        break

# Video akışını ve çıkış dosyasını serbest bırakın
cap.release()
out.release()

# Tüm pencereleri kapatın
cv2.destroyAllWindows()
