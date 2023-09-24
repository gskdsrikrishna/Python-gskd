#Countdown Timer for New Year's Eve:
import datetime
import time

def countdown_to_new_year():
    current_year = datetime.datetime.now().year
    new_year = datetime.datetime(current_year + 1, 1, 1)
    while True:
        current_time = datetime.datetime.now()
        time_remaining = new_year - current_time

        if time_remaining.total_seconds() <= 0:
            print("Happy New Year!")
            break

        days = time_remaining.days
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        time.sleep(1)

countdown_to_new_year()