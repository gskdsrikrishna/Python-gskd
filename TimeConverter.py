#Time Converter for Different Measurement Units:
def seconds_to_minutes(seconds):
    return seconds / 60

def hours_to_days(hours):
    return hours / 24

# Example usage:
seconds = 3600
minutes = seconds_to_minutes(seconds)
print(f"{seconds} seconds = {minutes} minutes")

hours = 48
days = hours_to_days(hours)
print(f"{hours} hours = {days} days")