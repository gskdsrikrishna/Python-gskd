#Automate email sending using PyAutoGUI:
import pyautogui
import time

# Open email application
pyautogui.press('win')
pyautogui.write('outlook')
pyautogui.press('enter')

# Wait for email application to open
time.sleep(5)

# Compose a new email
pyautogui.hotkey('ctrl', 'n')
time.sleep(2)

# Fill in recipient, subject, and body
pyautogui.write('example@example.com')
pyautogui.press('tab')
pyautogui.write('Test Email')
pyautogui.press('tab')
pyautogui.write('This is a test email.')
time.sleep(2)

# Send the email
pyautogui.hotkey('ctrl', 'enter')