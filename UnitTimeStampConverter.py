#Unix Timestamp Converter:
import datetime

def convert_to_unix_timestamp(datetime_obj):
    return int(datetime_obj.timestamp())

def convert_from_unix_timestamp(unix_timestamp):
    return datetime.datetime.fromtimestamp(unix_timestamp)

# Example usage:
current_datetime = datetime.datetime.now()
unix_timestamp = convert_to_unix_timestamp(current_datetime)
print(f"Unix Timestamp: {unix_timestamp}")

converted_datetime = convert_from_unix_timestamp(unix_timestamp)
print(f"Converted DateTime: {converted_datetime}")