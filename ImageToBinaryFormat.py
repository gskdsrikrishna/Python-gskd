#Convert an image to a binary format:
import cv2
image = cv2.imread("D:/Gskd-1.jpg", cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()