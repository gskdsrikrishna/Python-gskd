#Program PyAutoGUI to perform image recognition and automation:
import pyautogui
import time

# Wait for the target image to appear on the screen
target_image = '"C:/Users/GS.Devarayulu/OneDrive/Pictures/Gskd/Gskd-1.jpg"'
timeout = 10
start_time = time.time()
while time.time() - start_time < timeout:
    location = pyautogui.locateOnScreen(target_image)
    if location:
        break
    time.sleep(1)

if location:
    # Click on the target image
    center_x = location.left + location.width / 2
    center_y = location.top + location.height / 2
    pyautogui.click(center_x, center_y)
else:
    print("Target image not found within the specified timeout.")