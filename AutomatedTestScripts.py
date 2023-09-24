#Program PyAutoGUI to create automated test scripts for GUI applications:
import pyautogui
import time

# Open the GUI application
pyautogui.press('win')
pyautogui.write('calculator')
pyautogui.press('enter')

# Wait for the application to open
time.sleep(3)

# Perform some operations
pyautogui.press('1')
pyautogui.press('+')
pyautogui.press('2')
pyautogui.press('enter')

# Check the result
time.sleep(1)
result = pyautogui.locateOnScreen('result.png')
if result:
    print('Test passed: Addition performed correctly.')
else:
    print('Test failed: Addition result not found.')