#68.Check if a number is a perfect square
import math

def is_perfect_square(number):
    sqrt = math.isqrt(number)
    return sqrt * sqrt == number

# Example usage:
number = int(input("Enter a number: "))
if is_perfect_square(number):
    print(number, "is a perfect square.")
else:
    print(number, "is not a perfect square.")