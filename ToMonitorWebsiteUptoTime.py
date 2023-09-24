#Create a PyAutoGUI program to monitor website uptime:
import pyautogui
import requests
import time

# Define the URL of the website to monitor
url = 'https://www.example.com'

# Set the desired interval between checks (in seconds)
check_interval = 60

while True:
    # Send a GET request to the website
    response = requests.get(url)

    if response.status_code == 200:
        print(f"{url} is up and running!")
    else:
        print(f"{url} is down!")

    # Wait for the next check
    time.sleep(check_interval)