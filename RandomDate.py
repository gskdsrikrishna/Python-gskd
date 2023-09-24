import random
import datetime

def generate_random_date(start_date, end_date):
    start_timestamp = start_date.timestamp()
    end_timestamp = end_date.timestamp()
    random_timestamp = random.uniform(start_timestamp, end_timestamp)
    random_date = datetime.datetime.fromtimestamp(random_timestamp)
    return random_date

# Example usage:
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
random_date = generate_random_date(start_date, end_date)
print(random_date)
