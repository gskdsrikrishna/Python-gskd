#78.Check if a number is a repunit number
def is_repunit_number(number):
    repunit = int("1" * number)
    return repunit % number == 0

# Example usage:
number = int(input("Enter a number: "))
if is_repunit_number(number):
    print(number, "is a repunit number.")
else:
    print(number, "is not a repunit number.")