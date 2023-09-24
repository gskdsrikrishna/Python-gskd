#Daily Planner with Time Slots:
import datetime

class DailyPlanner:
    def __init__(self):
        self.schedule = {}

    def add_event(self, start_time, end_time, event):
        if start_time.date() != end_time.date():
            raise ValueError("Event cannot span multiple days")

        date = start_time.date()
        if date not in self.schedule:
            self.schedule[date] = []

        self.schedule[date].append({
            "start_time": start_time.time(),
            "end_time": end_time.time(),
            "event": event
        })

    def get_events_for_date(self, date):
        if date in self.schedule:
            return self.schedule[date]
        else:
            return []

# Example usage:
planner = DailyPlanner()
planner.add_event(datetime.datetime(2023, 6, 24, 9, 0), datetime.datetime(2023, 6, 24, 11, 0), "Meeting")
planner.add_event(datetime.datetime(2023, 6, 24, 13, 0), datetime.datetime(2023, 6, 24, 14, 30), "Lunch")
events = planner.get_events_for_date(datetime.date(2023, 6, 24))
for event in events:
    print(f"{event['start_time']} - {event['end_time']}: {event['event']}")