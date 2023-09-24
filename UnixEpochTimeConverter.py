#Unix Epoch Time Converter:
import datetime

def convert_to_unix_epoch_time(datetime_obj):
    return int(datetime_obj.timestamp())

def convert_from_unix_epoch_time(unix_epoch_time):
    return datetime.datetime.fromtimestamp(unix_epoch_time)

# Example usage:
current_datetime = datetime.datetime.now()
unix_epoch_time = convert_to_unix_epoch_time(current_datetime)
print(f"Unix Epoch Time: {unix_epoch_time}")

converted_datetime = convert_from_unix_epoch_time(unix_epoch_time)
print(f"Converted DateTime: {converted_datetime}")