#Automate web browser operations using PyAutoGUI:
import pyautogui
import time

# Open web browser
pyautogui.press('win')
time.sleep(2)
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')

# Wait for browser to open
time.sleep(4)

# Search for a query
pyautogui.write('google.com')
pyautogui.press('enter')

# Click on the first search result
time.sleep(3)
pyautogui.click(370, 550)
time.sleep(5)
pyautogui.click(700,775)