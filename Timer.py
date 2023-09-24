#Timer:
import time

def timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    print(f"Timer set for {duration} seconds.")

    while True:
        current_time = time.time()
        remaining_time = end_time - current_time

        if remaining_time <= 0:
            print("Time's up!")
            break

        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)

        print(f"Time remaining: {minutes:02d}:{seconds:02d}")
        time.sleep(1)

# Example usage: Set a timer for 5 minutes (300 seconds)
timer(10)