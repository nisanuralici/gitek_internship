# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:32:55 2023

@author: Nisanur
"""

import cv2
import numpy as np
#from google.colab.patches import cv2_imshow

# Load YOLOv4 model
net = cv2.dnn.readNet("/content/drive/MyDrive/yolov4.weights", "/content/drive/MyDrive/yolov4.cfg")
classes = []
with open("/content/drive/MyDrive/cocoNames/coco.names", "r") as f:
    classes = f.read().rstrip("\n").split("\n")
layer_names = net.getUnconnectedOutLayersNames()

# Initialize video capture
cap = cv2.VideoCapture("/content/drive/MyDrive/man.mp4")
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(classes), 3))
object_trackers = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, channels = frame.shape

    # Perform object detection
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(layer_names)

    # Extract information about detected objects
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-maximum suppression to eliminate redundant overlapping boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Update object trackers and draw bounding boxes
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            confidence = confidences[i]

            if label not in object_trackers:
                object_trackers[label] = cv2.TrackerCSRT_create()
                object_trackers[label].init(frame, (x, y, w, h))

            success, new_box = object_trackers[label].update(frame)
            if success:
                x, y, w, h = [int(v) for v in new_box]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 10), font, 1, color, 2)

    cv2.imshow(frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
