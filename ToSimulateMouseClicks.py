#Program PyAutoGUI to simulate mouse clicks:
import pyautogui

# Click the mouse at a specific coordinate
pyautogui.click(100, 200)

# Double-click the mouse at a specific coordinate
pyautogui.doubleClick(300, 400)

# Right-click the mouse at a specific coordinate
pyautogui.rightClick(500, 600)

# Simulate a mouse drag and drop operation
pyautogui.moveTo(700, 800)
pyautogui.dragTo(900, 1000, duration=1)