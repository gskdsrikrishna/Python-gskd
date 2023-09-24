#Time-based Birthday Reminder:
import datetime

def set_birthday_reminder(birthday):
    current_date = datetime.date.today()
    reminder_date = datetime.date(current_date.year, birthday.month, birthday.day)

    if reminder_date < current_date:
        reminder_date = datetime.date(current_date.year + 1, birthday.month, birthday.day)

    days_until_birthday = (reminder_date - current_date).days
    print(f"Days until next birthday: {days_until_birthday}")

# Example usage: Set a reminder for a birthday on August 1st
birthday = datetime.date(datetime.date.today().year, 8, 1)
set_birthday_reminder(birthday)