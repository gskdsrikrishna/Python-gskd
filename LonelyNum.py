#77.Check if a number is a lonely number
def is_lonely_number(number):
    return bin(number).count('1') == 1

# Example usage:
number = int(input("Enter a number: "))
if is_lonely_number(number):
    print(number, "is a lonely number.")
else:
    print(number, "is not a lonely number.")