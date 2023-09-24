import datetime
import time

def digital_clock():
    while True:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        print(formatted_time)
        time.sleep(1)

digital_clock()