#Create a PyAutoGUI program to extract data from PDF files:
import pyautogui
import time

# Open the PDF file
pyautogui.press('win')
pyautogui.write('Acrobat Reader')
pyautogui.press('enter')

# Wait for the application to open
time.sleep(5)

# Open the PDF file
pyautogui.hotkey('ctrl', 'o')
time.sleep(1)
pyautogui.write('Community Gskd.pdf')
pyautogui.press('enter')

# Wait for the PDF file to load
time.sleep(5)

# Extract text from the PDF file
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')

# Get the copied text from the clipboard
extracted_text = pyautogui.paste()
print(extracted_text)