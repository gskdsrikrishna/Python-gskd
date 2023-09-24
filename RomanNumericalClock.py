#Roman Numeral Clock:
import datetime

def convert_to_roman_numeral(number):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    for value, symbol in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    return roman_numeral

def convert_to_roman_numeral_time(time):
    hours = convert_to_roman_numeral(time.hour % 12 or 12)
    minutes = convert_to_roman_numeral(time.minute)
    seconds = convert_to_roman_numeral(time.second)

    return hours, minutes, seconds

# Example usage:
current_time = datetime.datetime.now().time()
roman_numeral_hours, roman_numeral_minutes, roman_numeral_seconds = convert_to_roman_numeral_time(current_time)
print(f"Roman Numeral Time: {roman_numeral_hours}:{roman_numeral_minutes}:{roman_numeral_seconds}")