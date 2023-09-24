#Generate and apply image gradients:
import cv2

image = cv2.imread("D:/Gskd-1.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate gradients using the Sobel operator
gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

# Apply gradient magnitude and orientation calculations
magnitude = cv2.magnitude(gradient_x, gradient_y)
angle = cv2.phase(gradient_x, gradient_y, angleInDegrees=True)

cv2.imshow('Gradient Magnitude', magnitude)
cv2.imshow('Gradient Angle', angle)
cv2.waitKey(0)
cv2.destroyAllWindows()