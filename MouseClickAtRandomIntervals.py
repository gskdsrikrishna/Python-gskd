#Simulate a mouse click at random intervals:
import pyautogui
import random
import time

# Generate random intervals between clicks
min_interval = 1  # Minimum interval in seconds
max_interval = 5  # Maximum interval in seconds

while True:
    # Simulate a mouse click
    pyautogui.click()

    # Generate a random interval
    interval = random.uniform(min_interval, max_interval)
    
    # Wait for the specified interval
    time.sleep(interval)