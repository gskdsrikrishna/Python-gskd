#Alarm Clock:
import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M")
        if formatted_time == alarm_time:
            print("Wake up!")
            # Play a sound (Windows only)
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        time.sleep(1)

# Example usage: set an alarm for 8:00 AM
set_alarm("12:27")