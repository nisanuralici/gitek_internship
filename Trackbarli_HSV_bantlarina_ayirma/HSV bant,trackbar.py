import cv2

def on_hue_change(value):
    global hsv_image
    hsv_image[:, :, 0] = value
    bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV Image', bgr_image)
def on_saturation_change(value):
    global hsv_image
    hsv_image[:, :, 1] = value
    bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV Image', bgr_image)
def on_value_change(value):
    global hsv_image
    hsv_image[:, :, 2] = value
    bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)
    cv2.namedWindow("HSV Image",cv2.WINDOW_NORMAL)
    cv2.imshow('HSV Image', bgr_image)
image = cv2.imread("C:/Users/Nisanur/Desktop/intern tasks/img1.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
initial_hue = 0
initial_saturation = 0
initial_value = 100
cv2.namedWindow('HSV Image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('Hue', 'HSV Image', initial_hue, 179, on_hue_change)
cv2.createTrackbar('Saturation', 'HSV Image', initial_saturation, 255, on_saturation_change)
cv2.createTrackbar('Value', 'HSV Image', initial_value, 255, on_value_change)
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  
        break
cv2.destroyAllWindows()
