#Time Duration Calculator:
import datetime

def calculate_time_duration(start_time, end_time):
    duration = end_time - start_time
    days = duration.days
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"Duration: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# Example usage: Calculate duration between two dates
start_time = datetime.datetime(2023, 6, 1, 8, 0, 0)
end_time = datetime.datetime(2023, 6, 30, 17, 30, 0)
calculate_time_duration(start_time, end_time)