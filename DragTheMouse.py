#Drag the mouse from one coordinate to another:
import pyautogui

start_x = 500  # Starting X-coordinate
start_y = 300  # Starting Y-coordinate
end_x = 800    # Ending X-coordinate
end_y = 600    # Ending Y-coordinate

pyautogui.moveTo(start_x, start_y)
pyautogui.dragTo(end_x, end_y, duration=1)