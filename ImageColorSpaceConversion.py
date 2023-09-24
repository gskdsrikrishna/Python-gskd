#Apply image color space conversion and manipulation:
import cv2

image = cv2.imread("D:/Gskd-1.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split the HSV image into individual channels
h, s, v = cv2.split(hsv_image)

# Apply histogram equalization to the grayscale image
equalized_image = cv2.equalizeHist(gray_image)

cv2.imshow('Grayscale', gray_image)
cv2.imshow('HSV', hsv_image)
cv2.imshow('Equalized', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()