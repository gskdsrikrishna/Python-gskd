#Pomodoro Timer:
import time

def pomodoro_timer(work_duration, break_duration, num_cycles):
    for cycle in range(num_cycles):
        print(f"Cycle {cycle+1}: Work")
        countdown(work_duration, "Work")

        if cycle < num_cycles - 1:
            print("Take a break")
            countdown(break_duration, "Break")

def countdown(duration, label):
    end_time = time.time() + duration * 60
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"{label} time remaining: {minutes:02d}:{seconds:02d}")
        time.sleep(1)
    print(f"{label} time finished!")

# Example usage: Pomodoro timer with 25 minutes of work, followed by a 5-minute break, for 4 cycles
pomodoro_timer(25, 5, 4)