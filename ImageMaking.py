#Apply image masking:
import cv2
import numpy as np
image = cv2.imread("D:/Gskd-1.jpg")
mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (10,20), (100+90, 200+10), 255, thickness=-1)  # Draw a filled rectangle on the mask
masked_image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()