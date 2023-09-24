import cv2

# Load the image
image = cv2.imread('image.jpg')

# Compress the image using JPEG compression
jpeg_params = [cv2.IMWRITE_JPEG_QUALITY, 80]  # Adjust the quality parameter as desired
success, compressed_image = cv2.imencode('.jpg', image, jpeg_params)

# Save the compressed image
cv2.imwrite('compressed_image.jpg', compressed_image)

# Compress the image using PNG compression
png_params = [cv2.IMWRITE_PNG_COMPRESSION, 9]  # Adjust the compression level (0-9) as desired
success, compressed_image = cv2.imencode('.png', image, png_params)

# Save the compressed image
cv2.imwrite('compressed_image.png', compressed_image)
