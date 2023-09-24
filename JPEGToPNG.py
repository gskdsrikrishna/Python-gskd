import cv2

# Load the image
image = cv2.imread('image.jpg')

# Define the output format (e.g., 'png', 'jpeg')
output_format = 'png'

# Convert the image to the desired format
converted_image = cv2.imencode('.' + output_format, image)[1].tobytes()

# Save the converted image
cv2.imwrite('converted_image.' + output_format, converted_image)
