import cv2 as cv
import numpy as np
import random
# Load the input image
img = cv.imread('doghuman.jpg')
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
net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
# Generate random colors for each class
classColors = []
for _ in range(len(classNames)):
    color = [random.randint(0, 255) for _ in range(3)]
    classColors.append(color)
# Process the image
blob = cv.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
net.setInput(blob)
layersNames = net.getLayerNames()
outputNames = [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
outputs = net.forward(outputNames)
# Find and draw objects
hT, wT, cT = img.shape
bbox = []
classIds = []
confs = []
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
indices = cv.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)
for i in indices:
    i = i[0]
    box = bbox[i]
    x, y, w, h = box[0], box[1], box[2], box[3]
    color = classColors[classIds[i]]
    cv.rectangle(img, (x, y), (x + w, y + h), color, 3)
    cv.rectangle(img, (x, y - 30), (x + 200, y), color, -1)  
    className = classNames[classIds[i]]
    label = f'{className.upper()} {int(confs[i] * 100)}%'
    cv.putText(img, label, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 3)
# Display the image with detected objects
cv.namedWindow('Image', cv.WINDOW_NORMAL)
cv.imshow('Image', img)

# Save the image with detected objects
output_filename = 'detected_objects.jpg'  # İstediğiniz bir dosya adı belirleyin
cv.imwrite(output_filename, img)

cv.waitKey(0)  # Wait until a key is pressed
cv.destroyAllWindows()
