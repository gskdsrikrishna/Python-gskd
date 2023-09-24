#Simulate typing a string of text with random intervals:
import pyautogui
import random
import time

text = "Hello, world!"

# Iterate through each character in the text
for char in text:
    # Simulate typing the current character
    pyautogui.typewrite(char)

    # Generate a random interval between keystrokes
    interval = random.uniform(0.1, 0.3)

    # Wait for the specified interval
    time.sleep(interval)