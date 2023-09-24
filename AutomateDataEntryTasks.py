#Automate data entry tasks using PyAutoGUI:
import pyautogui
import time

# Open the target application
pyautogui.press('win')
time.sleep(2)
pyautogui.write('notepad')
time.sleep(2)
pyautogui.press('enter')

# Wait for the application to open
time.sleep(2)

# Enter data into the application
pyautogui.write("<html><head><title>Python</title></head><body><h1>Gskd</h1></body></html>")
time.sleep(10)

# Save the entered data
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
pyautogui.write('python.txt')
time.sleep(2)
pyautogui.press('enter')