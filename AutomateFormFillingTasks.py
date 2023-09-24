#Automate form filling tasks using PyAutoGUI
import pyautogui
import time

# Move the mouse to the first form field
pyautogui.moveTo(500, 300)

# Fill in the form fields
pyautogui.write('John Doe')
pyautogui.press('tab')
pyautogui.write('johndoe@example.com')
pyautogui.press('tab')
pyautogui.write('Password123')
pyautogui.press('tab')
pyautogui.write('1234567890')

# Submit the form
pyautogui.press('enter')