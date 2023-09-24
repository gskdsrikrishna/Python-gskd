#Time Elapsed Calculator for Work Hours:
import datetime

class WorkDay:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def end(self):
        self.end_time = datetime.datetime.now()

    def get_work_hours(self):
        if self.start_time and self.end_time:
            work_hours = self.end_time - self.start_time
            return work_hours.total_seconds() / 3600  # Convert to hours
        else:
            return 0

# Example usage:
workday = WorkDay()
workday.start()
# Perform work tasks...
workday.end()
hours_worked = workday.get_work_hours()
print(f"Hours worked: {hours_worked} hours")