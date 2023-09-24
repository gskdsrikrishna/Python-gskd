#Get the current position of the mouse cursor:
import pyautogui

# Get the current position of the mouse cursor
x, y = pyautogui.position()

print(f"Current position: X={x}, Y={y}")