#Apply image blurring
import cv2
image = cv2.imread("D:/Gskd-1.jpg")
blurred_image = cv2.blur(image, (10,10))  # Apply a simple averaging blur
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()