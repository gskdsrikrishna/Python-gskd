#69.Check if a number is Kaprekar
def is_kaprekar_number(number):
    square = number * number
    str_square = str(square)
    length = len(str_square)

    for i in range(1, length):
        part1 = int(str_square[:i])
        part2 = int(str_square[i:])

        if part1 + part2 == number:
            return True

    return False

# Example usage:
number = int(input("Enter a number: "))
if is_kaprekar_number(number):
    print(number, "is a Kaprekar number.")
else:
    print(number, "is not a Kaprekar number.")