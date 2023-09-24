#Event Countdown Timer:
import datetime
import time

def countdown_to_event(event_date):
    while True:
        current_time = datetime.datetime.now()
        time_remaining = event_date - current_time

        if time_remaining.total_seconds() <= 0:
            print("Event time reached!")
            break

        days = time_remaining.days
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        time.sleep(1)

# Example usage: Countdown to December 31, 2023, 12:00 PM
event_date = datetime.datetime(2023, 12, 31, 12, 0, 0)
countdown_to_event(event_date)