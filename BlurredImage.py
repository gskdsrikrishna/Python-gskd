import cv2
image = cv2.imread("C:/Users/GS.Devarayulu/OneDrive/Pictures/Gskd/VideoCapture_20230327-171835.jpg")
blurred_image = cv2.blur(image, (10, 10))  # Apply a simple averaging blur
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()