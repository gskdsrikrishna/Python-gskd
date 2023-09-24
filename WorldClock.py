#World Clock:
import datetime
import pytz

def world_clock(time_zones):
    while True:
        current_time = datetime.datetime.now()
        for tz in time_zones:
            time_zone = pytz.timezone(tz)
            formatted_time = current_time.astimezone(time_zone).strftime("%Y-%m-%d %H:%M:%S")
            print(f"{tz}: {formatted_time}")
        print("------------------------")
        time.sleep(1)

# Example usage: Display current time in New York, London, and Tokyo
time_zones = ["America/New_York", "Europe/London", "Asia/Tokyo"]
world_clock(time_zones)