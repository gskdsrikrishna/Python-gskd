#71.Check if a number is a narcisstic number
def is_narcissistic_number(number):
    num_str = str(number)
    power = len(num_str)
    sum_of_powers = sum(int(digit) ** power for digit in num_str)
    return number == sum_of_powers

# Example usage:
number = int(input("Enter a number: "))
if is_narcissistic_number(number):
    print(number, "is a narcissistic number.")
else:
    print(number, "is not a narcissistic number.")