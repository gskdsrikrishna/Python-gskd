#Simulate a mouse click at random coordinates on the screen:
import pyautogui
import random

# Get the screen resolution
screen_width, screen_height = pyautogui.size()

# Generate random coordinates within the screen bounds
random_x = random.randint(0, screen_width)
random_y = random.randint(0, screen_height)

# Simulate a mouse click at the random coordinates
pyautogui.click(random_x, random_y)