#Apply image thresholding:
import cv2
image = cv2.imread("D:/Gskd-1.jpg", cv2.IMREAD_GRAYSCALE)
_, thresholded_image = cv2.threshold(image, 150, 300, cv2.THRESH_BINARY)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()