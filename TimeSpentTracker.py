#Time Spent Tracker for Tasks:
import datetime

class Task:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def end(self):
        self.end_time = datetime.datetime.now()

    def get_duration(self):
        if self.start_time and self.end_time:
            duration = self.end_time - self.start_time
            return duration.total_seconds() / 60  # Convert to minutes
        else:
            return 0

# Example usage:
task = Task("Coding")
task.start()
# Perform the task...
task.end()
duration = task.get_duration()
print(f"Task: {task.name}")
print(f"Duration: {duration} minutes")