#Islamic Prayer Times Calculator:
import requests

def get_prayer_times(latitude, longitude):
    url = f"http://api.aladhan.com/v1/calendar?latitude={latitude}&longitude={longitude}&method=2"
    response = requests.get(url)
    data = response.json()
    prayer_times = data['data'][0]['timings']
    return prayer_times

latitude = 40.7128
longitude = -74.0060
prayer_times = get_prayer_times(latitude, longitude)

for prayer, time in prayer_times.items():
    print(f"{prayer}: {time}")