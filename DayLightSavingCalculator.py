#Daylight Saving Time Calculator:
import datetime
import pytz

def is_daylight_saving_time(datetime_obj, timezone):
    timezone = pytz.timezone(timezone)
    return timezone.dst(datetime_obj) != datetime.timedelta(0)

# Example usage:
current_datetime = datetime.datetime.now()
timezone = "America/New_York"
is_dst = is_daylight_saving_time(current_datetime, timezone)
print(f"Is Daylight Saving Time: {is_dst}")