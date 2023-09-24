from PIL import Image, ImageDraw
import random

def generate_random_image(width, height):
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    for _ in range(1000):  # Adjust the number of iterations to change the density of dots
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.point((x, y), fill=color)

    return image

# Example usage:
image_width = 800
image_height = 600
random_image = generate_random_image(image_width, image_height)
random_image.show()
