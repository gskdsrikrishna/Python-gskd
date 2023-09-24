#Take a screenshot of a specific region on the screen:
import pyautogui

x = 100  # X-coordinate of the top-left corner of the region
y = 100  # Y-coordinate of the top-left corner of the region
width = 300  # Width of the region
height = 200  # Height of the region

# Capture the specified region of the screen
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# Save the screenshot as an image file
screenshot.save('region_screenshot.png')