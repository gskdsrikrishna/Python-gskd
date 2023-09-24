#Resize an image:
import cv2
image = cv2.imread("D:/Gskd-1.jpg")
resized_image = cv2.resize(image, (100, 100))
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()