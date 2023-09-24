#Flip an image horizontally or vertically:
import cv2
image = cv2.imread("D:/Gskd-1.jpg")
flipped_horizontal = cv2.flip(image, 1)  # Flip horizontally
flipped_vertical = cv2.flip(image, 0)  # Flip vertically
cv2.imshow('Flipped Horizontal', flipped_horizontal)
cv2.imshow('Flipped Vertical', flipped_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()