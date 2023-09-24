#Read and display an image:
import cv2
image = cv2.imread("D:/Gskd-1.jpg")
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()