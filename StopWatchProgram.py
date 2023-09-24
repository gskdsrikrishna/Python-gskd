#Stopwatch:
import time

def stopwatch():
    start_time = time.time()
    print("Stopwatch started. Press Enter to stop.")
    input()

    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

stopwatch()