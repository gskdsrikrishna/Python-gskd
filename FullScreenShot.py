import pyautogui
# Capture a full screenshot
screenshot = pyautogui.screenshot()
screenshot.save("full_screenshot.png")
# Capture a specific region of the screen
x, y, width, height = 100, 100, 500, 300
region_screenshot = pyautogui.screenshot(region=(x, y, width, height))
region_screenshot.save("D:/GskdPy/region.png")