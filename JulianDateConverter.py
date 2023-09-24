#Julian Date Converter:
import datetime

def convert_to_julian_date(datetime_obj):
    start_of_year = datetime.datetime(datetime_obj.year, 1, 1)
    julian_day = (datetime_obj - start_of_year).days + 1
    return datetime_obj.year, julian_day

def convert_from_julian_date(year, julian_day):
    start_of_year = datetime.datetime(year, 1, 1)
    return start_of_year + datetime.timedelta(days=julian_day-1)

# Example usage:
current_datetime = datetime.datetime.now()
year, julian_day = convert_to_julian_date(current_datetime)
print(f"Julian Date: {year}-{julian_day}")

converted_datetime = convert_from_julian_date(year, julian_day)
print(f"Converted DateTime: {converted_datetime}")