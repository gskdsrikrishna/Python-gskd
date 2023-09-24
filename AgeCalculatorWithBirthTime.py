#Age Calculator with Birth Time:
import datetime

def calculate_age(birth_date):
    current_date = datetime.datetime.now().date()
    age = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    return age

birth_date = datetime.date(1990, 5, 1)
age = calculate_age(birth_date)
print(f"Age: {age} years")