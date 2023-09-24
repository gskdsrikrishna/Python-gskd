#Detect and draw edges in an image:
import cv2
image = cv2.imread("D:/Gskd-1.jpg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 80, 80)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()