#70.Check if a number is a happy prime number
def is_happy_prime(number):
    return is_happy_number(number) and is_prime(number)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage:
number = int(input("Enter a number: "))
if is_happy_prime(number):
    print(number, "is a happy prime number.")
else:
    print(number, "is not a happy prime number.")