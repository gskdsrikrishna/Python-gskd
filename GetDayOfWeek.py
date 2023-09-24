import datetime

def get_day_of_week(year, month, day):
    input_date = datetime.date(year, month, day)
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_of_week = days_of_week[input_date.weekday()]
    return day_of_week

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

day_of_week = get_day_of_week(year, month, day)
print("Day of the Week:", day_of_week)
