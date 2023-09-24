#Time Zone Converter:
import datetime
import pytz

def convert_timezone(datetime_obj, from_timezone, to_timezone):
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)
    localized_datetime = from_tz.localize(datetime_obj)
    converted_datetime = localized_datetime.astimezone(to_tz)
    return converted_datetime

# Example usage:
current_datetime = datetime.datetime.now()
from_timezone = "America/New_York"
to_timezone = "Asia/Tokyo"
converted_datetime = convert_timezone(current_datetime, from_timezone, to_timezone)
print(f"Converted DateTime: {converted_datetime}")