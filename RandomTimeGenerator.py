#Random Time Generator:
import random
import datetime

def generate_random_time():
    current_time = datetime.datetime.now()
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    random_time = current_time.replace(hour=random_hour, minute=random_minute, second=random_second)
    return random_time

random_time = generate_random_time()
print(random_time)