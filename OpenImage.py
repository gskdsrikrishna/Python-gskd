from PIL import Image

# Open the image file
image = Image.open("C:/Users/GS.Devarayulu/OneDrive/Pictures/Gskd/gskd1.jpg")

# Perform operations on the image
# For example, you can get information about the image
width, height = image.size
image_format = image.format

# You can also display the image
image.show()

# Remember to close the image after you're done
image.close()