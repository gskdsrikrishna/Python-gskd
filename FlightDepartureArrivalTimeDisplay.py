#Flight Departure and Arrival Time Display:
import datetime

def display_flight_time(departure_time, duration):
    arrival_time = departure_time + datetime.timedelta(minutes=duration)
    print(f"Departure time: {departure_time}")
    print(f"Arrival time: {arrival_time}")

# Example usage: Display flight time for a 2-hour duration flight
departure_time = datetime.datetime(2023, 6, 24, 8, 0, 0)
duration = 120  # 2 hours
display_flight_time(departure_time, duration)