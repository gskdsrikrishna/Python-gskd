#62.Find the count of digits in a number
def count_digits(number):
    return len(str(number))

# Example usage:
number = int(input("Enter a number: "))
digit_count = count_digits(number)
print("Number of digits:", digit_count)