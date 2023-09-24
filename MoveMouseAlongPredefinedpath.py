#Move the mouse along a predefined path on the screen:
import pyautogui

# Define the coordinates of the path
path = [(100, 100), (200, 300), (500, 200), (400, 100)]

# Move the mouse along the predefined path
for x, y in path:
    pyautogui.moveTo(x, y)