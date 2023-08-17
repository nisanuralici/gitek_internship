# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:11:43 2023

@author: Nisanur
"""
import cv2 
import numpy as np
import serial
import time
from pyfirmata import Arduino, util
board = Arduino("COM3")
# Load the input image
img = cv2.imread('people.jpg')

# YOLO parameters
whT = 320
confThreshold = 0.5
nmsThreshold = 0.3

# Load class names
classesFile = "C:/Users/Nisanur/Desktop/intern tasks/cocoNames/coco.names"  # Provide the correct path
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load YOLO model
modelConfiguration = "yolov3.cfg"  # Provide the correct path
modelWeights = "yolov3.weights"  # Provide the correct path
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


# Process the image
blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
net.setInput(blob)
layersNames = net.getLayerNames()
outputNames = [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
outputs = net.forward(outputNames)

# Find and draw objects
hT, wT, cT = img.shape
bbox = []
classIds = []
confs = []
yesil_led = 12
kirmizi_led= 13
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
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv2.rectangle(img, (x, y - 30), (x + 200, y), (0, 0, 255), -1)  
    cv2.putText(img, classNames[classIds[i]], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)
    #cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    if i < len(classIds) and i < len(confs) and i < len(bbox):
        className = classNames[classIds[i]]
        label = f'{className.upper()}'
        if className == "insan":
            cv2.putText(img, "insan var", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.9, (255, 255, 255), 8)
            board.digital[yesil_led].write(1) # Arduino'ya 1 göndererek LED'i yak
            board.digital[kirmizi_led].write(0)
            time.sleep(0.1)  # LED'i belirli bir süre sonra söndür
        else:
            cv2.putText(img, "insan yok", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.9, (255, 255, 255), 8)
            board.digital[kirmizi_led].write(1) # Arduino'ya 1 göndererek LED'i yak
            board.digital[yesil_led].write(0)
            time.sleep(0.1)
# Display the image with detected objects
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)

cv2.waitKey(0)  # Wait until a key is pressed
board.exit()
cv2.destroyAllWindows()

