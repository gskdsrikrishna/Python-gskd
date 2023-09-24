#65.Check if a number is a strong number
def is_strong_number(number):
    sum_of_factorial = 0
    original_number = number

    while number > 0:
        digit = number % 10
        sum_of_factorial += factorial(digit)
        number //= 10

    return sum_of_factorial == original_number

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Example usage:
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(number, "is a strong number.")
else:
    print(number, "is not a strong number.")