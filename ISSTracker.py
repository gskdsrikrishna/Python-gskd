#International Space Station (ISS) Tracker with Time Display:

import requests

def get_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    position = data["iss_position"]
    latitude = position["latitude"]
    longitude = position["longitude"]
    return latitude, longitude

latitude, longitude = get_iss_position()
print(f"Current ISS position: Latitude={latitude}, Longitude={longitude}")
