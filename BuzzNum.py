#67.Check if a number is a buzz number
def is_buzz_number(number):
    if number % 7 == 0 or number % 10 == 7:
        return True
    else:
        return False

# Example usage:
number = int(input("Enter a number: "))
if is_buzz_number(number):
    print(number, "is a buzz number.")
else:
    print(number, "is not a buzz number.")