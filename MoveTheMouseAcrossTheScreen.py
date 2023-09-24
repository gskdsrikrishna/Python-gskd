#Move the mouse in a smooth curve across the screen:
import pyautogui

# Define the curve parameters
center_x = 500  # X-coordinate of the curve center
center_y = 300  # Y-coordinate of the curve center
radius = 200    # Radius of the curve

# Move the mouse in a smooth curve across the screen
pyautogui.moveTo(center_x, center_y)
pyautogui.dragTo(center_x + radius, center_y, duration=1)  # Right point of the curve
pyautogui.dragTo(center_x, center_y + radius, duration=1)  # Bottom point of the curve
pyautogui.dragTo(center_x - radius, center_y, duration=1)  # Left point of the curve
pyautogui.dragTo(center_x, center_y - radius, duration=1)  # Top point of the curve