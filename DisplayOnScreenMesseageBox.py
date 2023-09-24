#Display an on-screen message box:
import pyautogui

message = "Hello, world!"
title = "Message Box"
button = "OK"

# Display an on-screen message box
pyautogui.alert(text=message, title=title, button=button)