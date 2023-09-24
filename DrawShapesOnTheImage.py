#Draw shapes on an image (lines, rectangles, circles):
import cv2
image = cv2.imread("D:/Gskd-1.jpg")
# Draw a line
cv2.line(image, (100,200), (200,300), (0, 255, 0), 5)
# Draw a rectangle
cv2.rectangle(image, (50,100), (150,200), (0, 0, 255), 5)
# Draw a circle
cv2.circle(image, (250,250), 25, (255, 0, 0),5)
cv2.imshow('Image with Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()