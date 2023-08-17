import cv2
import numpy as np

def nothing(x):
    pass
#video yükleme
cap = cv2.VideoCapture('video3.mp4')
# Sonuç videosunu kaydetme için yapılandırma
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
#trackbar oluşturma
cv2.namedWindow('Trackbars')
cv2.createTrackbar("Hue Low", 'Trackbars', 0, 179, nothing)
cv2.createTrackbar("Hue High", 'Trackbars', 179, 179, nothing)
cv2.createTrackbar("Saturation Low", 'Trackbars', 0,255, nothing)
cv2.createTrackbar("Saturation High", 'Trackbars', 255,255, nothing)
cv2.createTrackbar("Value Low", 'Trackbars', 0,255, nothing)
cv2.createTrackbar("Value High", 'Trackbars', 255,255, nothing)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    #HSV ye dönüştürne
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #trackbar değerleri
    hue_low = cv2.getTrackbarPos('Hue Low', 'Trackbars')
    hue_high = cv2.getTrackbarPos('Hue High', 'Trackbars')
    saturation_low = cv2.getTrackbarPos('Saturation Low', 'Trackbars')
    saturation_high = cv2.getTrackbarPos('Saturation High', 'Trackbars')
    value_low = cv2.getTrackbarPos('Value Low', 'Trackbars')
    value_high = cv2.getTrackbarPos('Value High', 'Trackbars')
    #HSV bantlarını ayırma
    lower_bound = np.array([hue_low, saturation_low, value_low])
    upper_bound = np.array([hue_high, saturation_high, value_high])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    #görüntüleri gösterme
    # Sonuç videosuna kaydetme
    out.write(result)
    #cv2.imshow('Original', frame)
    cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
    cv2.imshow("Original", frame)
    #cv2.imshow('Result', result)
    cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
    cv2.imshow("Result", result)
    if cv2.waitKey(500) & 0xFF == ord('w'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()