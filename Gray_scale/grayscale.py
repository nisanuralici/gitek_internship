import cv2
image = cv2.imread("img.jpg",0) #burada görseli okuttuktan sonra 1 yazarsa renkli, 0 yazarsa gri
cv2.imshow("gray image", image)
cv2.imwrite("siyah_beyaz_goruntu.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
