import cv2

image1 = cv2.imread("star.jpg")
image2 = cv2.imread("star1.jpg")

# Görüntü boyutlarını ve türlerini kontrol etme
if image1.shape == image2.shape and image1.dtype == image2.dtype:
    concatenated_image = cv2.hconcat([image1, image2])

    # Birleştirilmiş görüntüyü kaydet
    output_filename = "concatenated_image.jpg"
    cv2.imwrite(output_filename, concatenated_image)

    cv2.imshow("Concatenated Image", concatenated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Görüntülerin boyutları veya tipleri uyumsuz.")
