import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("man.mp4")

# Video ayarları
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.rectangle(frame, (x, y - 30), (x + 100, y), (0, 0, 255), -1)  
        cv2.putText(frame, 'human', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    out.write(frame)  # Görüntüyü kaydet
    cv2.namedWindow('Face Detection',cv2.WINDOW_NORMAL)
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

cap.release()
out.release()  # VideoWriter'ı kapat
cv2.destroyAllWindows()
