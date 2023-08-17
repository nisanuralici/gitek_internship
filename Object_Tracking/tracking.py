import cv2
import numpy as np

# Video yakalama
video_path = 'video8.mp4'
cap = cv2.VideoCapture(video_path)

# Sonuç videosunu kaydetme için yapılandırma
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out_result = cv2.VideoWriter('output_result_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Maske videosunu kaydetme için yapılandırma
out_mask = cv2.VideoWriter('output_mask_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height), isColor=False)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # HSV renk uzayına dönüştürme
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Yeşil renk aralığı (örnek olarak)
    lower_value = np.array([35, 50, 50])
    upper_value = np.array([85, 255, 255])
    
    # Maske oluşturma
    green_mask = cv2.inRange(hsv_frame, lower_value, upper_value)
    
    # Maske videosuna kaydetme
    out_mask.write(green_mask)
    
    # Kontur tespiti
    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_area_threshold = 100
    for contour in contours:
        # Kontur alanına göre filtreleme yapabilirsiniz
        if cv2.contourArea(contour) > min_area_threshold:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Sonuç videosuna kaydetme
    out_result.write(frame)
    
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

# Video akışını ve çıkış dosyalarını serbest bırakma
cap.release()
out_result.release()
out_mask.release()

# Tüm pencereleri kapatma
cv2.destroyAllWindows()
