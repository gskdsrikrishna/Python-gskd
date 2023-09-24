import datetime

def is_valid_date(year, month, day):
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

if is_valid_date(year, month, day):
    print("Valid date.")
else:
    print("Invalid date.")
