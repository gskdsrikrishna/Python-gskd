#24-hour Clock Converter:
import datetime

def convert_to_24_hour_clock(time):
    return time.strftime("%H:%M:%S")

# Example usage:
current_time = datetime.datetime.now().time()
converted_time = convert_to_24_hour_clock(current_time)
print(f"24-Hour Time: {converted_time}")