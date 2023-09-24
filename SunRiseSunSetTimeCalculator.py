#Sunrise and Sunset Time Calculator:
import datetime
import pytz
import requests

def get_sunrise_sunset(latitude, longitude, date):
    url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date={date}"
    response = requests.get(url)
    data = response.json()
    sunrise = datetime.datetime.strptime(data['results']['sunrise'], "%I:%M:%S %p")
    sunset = datetime.datetime.strptime(data['results']['sunset'], "%I:%M:%S %p")
    return sunrise, sunset

# Example usage:
latitude = 37.7749  # San Francisco latitude
longitude = -122.4194  # San Francisco longitude
date = datetime.date.today()
sunrise, sunset = get_sunrise_sunset(latitude, longitude, date)
print(f"Sunrise: {sunrise.time()}")
print(f"Sunset: {sunset.time()}")