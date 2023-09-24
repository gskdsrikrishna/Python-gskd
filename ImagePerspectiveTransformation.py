#Apply image perspective transformation:
import cv2
import numpy as np
image = cv2.imread("D:/Gskd-1.jpg")
height, width = image.shape[:2]
source_points = np.float32([[1,2], [2,3], [3,4], [4,5]])  # Define the source points
destination_points = np.float32([[50,60], [15,25], [25,35], [305,405]])  # Define the destination points
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)
transformed_image = cv2.warpPerspective(image, perspective_matrix, (width, height))
cv2.imshow('Perspective Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()