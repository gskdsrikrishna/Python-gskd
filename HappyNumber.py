#61.Check if a number is a happy number
def is_happy_number(number):
    seen_numbers = set()

    while number != 1:
        number = sum(int(digit) ** 2 for digit in str(number))
        if number in seen_numbers:
            return False
        seen_numbers.add(number)

    return True

# Example usage:
number = int(input("Enter a number: "))
if is_happy_number(number):
    print(number, "is a happy number.")
else:
    print(number, "is not a happy number.")