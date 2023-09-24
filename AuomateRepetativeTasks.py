#Create a bot using PyAutoGUI to automate repetitive tasks:
import pyautogui
import time

# Wait for the target window to appear
time.sleep(5)

# Move the mouse and click on specific coordinates
pyautogui.moveTo(100, 200)
pyautogui.click()
time.sleep(1)

# Type a string of text using the keyboard
pyautogui.typewrite('Hello, world!')
time.sleep(1)

# Press and release a specific key on the keyboard
pyautogui.press('enter')
time.sleep(1)

# Capture a screenshot and save it as an image
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')