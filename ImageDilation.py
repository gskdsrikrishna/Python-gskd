#Apply image dilation:
import cv2
import numpy as np
image = cv2.imread("D:/Gskd-1.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3,3), np.uint8)
dilated_image = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()