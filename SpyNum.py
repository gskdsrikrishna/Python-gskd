#66.Check if a number is a spy number
def is_spy_number(number):
    digit_sum = 0
    digit_product = 1

    while number > 0:
        digit = number % 10
        digit_sum += digit
        digit_product *= digit
        number //= 10

    return digit_sum == digit_product

# Example usage:
number = int(input("Enter a number: "))
if is_spy_number(number):
    print(number, "is a spy number.")
else:
    print(number, "is not a spy number.")