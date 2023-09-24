#76.Check if a number is a powerful number
def is_powerful_number(number):
    if number == 1:
        return True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            power = i
            while number % power == 0:
                number //= power
            if number == 1:
                return True
    return False

# Example usage:
number = int(input("Enter a number: "))
if is_powerful_number(number):
    print(number, "is a powerful number.")
else:
    print(number, "is not a powerful number.")