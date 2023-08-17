import cv2

cap = cv2.VideoCapture('video8.mp4')

while not cap.isOpened():
    pass

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_filename = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.putText(frame, f"Width: {width}, Height: {height}, FPS: {fps}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.imshow('Video', frame)

    out.write(frame)  # Çıktı videoya kareyi yaz

    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

cap.release()
out.release()  # Çıktı videoyu serbest bırak
cv2.destroyAllWindows()
