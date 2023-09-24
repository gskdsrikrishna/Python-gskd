#73.Check if a number is a vampire number
def is_vampire_number(number):
    num_str = str(number)
    num_len = len(num_str)
    num_digits = [int(digit) for digit in num_str]

    for factor1 in range(10**(num_len // 2 - 1), 10**(num_len // 2)):
        if number % factor1 == 0:
            factor2 = number // factor1
            if sorted(str(factor1) + str(factor2)) == sorted(num_str):
                return True

    return False

# Example usage:
number = int(input("Enter a number: "))
if is_vampire_number(number):
    print(number, "is a vampire number.")
else:
    print(number, "is not a vampire number.")