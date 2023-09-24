#Check if a specific color is present on the screen:
import pyautogui

# Check if the color is present on the screen
color = (255, 0, 0)  # RGB color (red)

if pyautogui.pixelMatchesColor(500, 300, color):
    print("Color found on the screen.")
else:
    print("Color not found on the screen.")