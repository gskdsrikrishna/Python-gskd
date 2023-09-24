#Rotate an image:
import cv2
image = cv2.imread("D:/Gskd-1.jpg")
rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)  # Define the rotation parameters
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()