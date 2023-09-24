#Get the current screen resolution:
import pyautogui

# Get the current screen resolution
screen_width, screen_height = pyautogui.size()

print(f"Screen resolution: {screen_width}x{screen_height}")