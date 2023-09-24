import cv2
image = cv2.imread("C:/Users/GS.Devarayulu/OneDrive/Pictures/Gskd/VideoCapture_20230327-171835.jpg")
# Draw a line
cv2.line(image, (0, 100), (200, 400), (0, 255, 0), 2)
# Draw a rectangle
cv2.rectangle(image, (0, 200), (0, 300), (0, 0, 255), 2)
# Draw a circle
cv2.circle(image, (10, 20), 10, (255, 0, 0), 2)
cv2.imshow('Image with Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()