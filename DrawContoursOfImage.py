#Find and draw contours in an image:
import cv2
image = cv2.imread("D:/Gskd-1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 70)
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()