#Meeting Scheduler:
import datetime

def find_available_time_slots(participant_calendars, meeting_duration):
    # Combine all participant calendars
    all_events = []
    for calendar in participant_calendars:
        all_events.extend(calendar)

    # Sort events by start time
    all_events.sort(key=lambda event: event["start"])

    available_slots = []
    start_time = datetime.datetime.now()

    for event in all_events:
        end_time = event["start"]
        if (end_time - start_time).total_seconds() >= meeting_duration * 60:
            available_slots.append((start_time, end_time))
        start_time = event["end"]

    # Check if there is time remaining after the last event
    if (datetime.datetime.now() - start_time).total_seconds() >= meeting_duration * 60:
        available_slots.append((start_time, datetime.datetime.max))

    return available_slots

# Example usage: Finding available time slots for a meeting of 1 hour (60 minutes)
participant_calendars = [
    [
        {"start": datetime.datetime(2023, 6, 24, 9, 0), "end": datetime.datetime(2023, 6, 24, 10, 0)},
        {"start": datetime.datetime(2023, 6, 24, 12, 0), "end": datetime.datetime(2023, 6, 24, 13, 0)}
    ],
    [
        {"start": datetime.datetime(2023, 6, 24, 9, 30), "end": datetime.datetime(2023, 6, 24, 10, 30)},
        {"start": datetime.datetime(2023, 6, 24, 11, 0), "end": datetime.datetime(2023, 6, 24, 12, 0)}
    ]
]

meeting_duration = 60

available_slots = find_available_time_slots(participant_calendars, meeting_duration)
print("Available time slots:")
for slot in available_slots:
    print(f"{slot[0]} - {slot[1]}")