#Get the color of a specific pixel on the screen:
import pyautogui

x = 500  # X-coordinate of the pixel
y = 300  # Y-coordinate of the pixel

# Get the color of the specified pixel on the screen
pixel_color = pyautogui.pixel(x, y)

print(f"Pixel color at ({x}, {y}): {pixel_color}")