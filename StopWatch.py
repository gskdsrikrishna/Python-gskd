import time

def stopwatch():
    start_time = time.time()
    input("Press Enter to stop the stopwatch.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time:", elapsed_time, "seconds")
stopwatch()a