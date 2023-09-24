#Apply image histogram equalization:
import cv2
image = cv2.imread("D:/Gskd-1.jpg", cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(image)
cv2.imshow('Histogram Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()