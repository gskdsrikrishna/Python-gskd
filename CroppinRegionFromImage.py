#Crop a region of interest from an image:
import cv2
image = cv2.imread("D:/Gskd-1.jpg")
roi = image[100:100+200, 200:200+300]  # Define the region of interest coordinates
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()