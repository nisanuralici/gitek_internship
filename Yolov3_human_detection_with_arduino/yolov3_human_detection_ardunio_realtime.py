import cv2 
import numpy as np
import serial
import time
from pyfirmata import Arduino, util

board = Arduino("COM4")

cap = cv2.VideoCapture(0)

# YOLO parametreler
whT = 320
confThreshold = 0.5
nmsThreshold = 0.3

classesFile = "C:/Users/Nisanur/Desktop/intern tasks/cocoNames/coco.names" 
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

#YOLO model
modelConfiguration = "yolov3.cfg"  
modelWeights = "yolov3.weights" 
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
    net.setInput(blob)
    layersNames = net.getLayerNames()
    outputNames = [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames)
    hT, wT, cT = frame.shape
    bbox = []
    classIds = []
    confs = []
    yesil_led = 12
    kirmizi_led = 13
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.rectangle(frame, (x, y - 30), (x + 200, y), (0, 0, 255), -1)  
        cv2.putText(frame, classNames[classIds[i]], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, 
                    (255, 255, 255), 3)
        if i < len(classIds) and i < len(confs) and i < len(bbox):
            className = classNames[classIds[i]]
            label = f'{className.upper()}'
            if className == "insan":
                cv2.putText(frame, "insan var", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.9, (0, 255, 0), 8)
                board.digital[yesil_led].write(1)  # Arduino'ya 1 göndererek LED'i yak
                board.digital[kirmizi_led].write(0)
                time.sleep(0.1)  # LED'i belirli bir süre sonra söndür
            else:
                cv2.putText(frame, "insan yok", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.9, (255, 255, 255),8)
                board.digital[kirmizi_led].write(1)  # Arduino'ya 1 göndererek LED'i yak
                board.digital[yesil_led].write(0)
                time.sleep(0.1)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

cap.release()
board.exit()
cv2.destroyAllWindows()

