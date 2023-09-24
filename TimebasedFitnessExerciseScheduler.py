#Time-based Fitness Exercise Scheduler:
import datetime
import winsound

def schedule_exercise(exercise_time):
    current_time = datetime.datetime.now().time()
    while current_time < exercise_time:
        current_time = datetime.datetime.now().time()

    # Play sound to indicate exercise time
    winsound.Beep(1000, 1000)

# Example usage: Schedule exercise at 8:00 AM
exercise_time = datetime.time(8, 0, 0)
schedule_exercise(exercise_time)