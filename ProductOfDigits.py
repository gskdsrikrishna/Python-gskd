#63.Calculate the product of digits in a number
def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

# Example usage:
number = int(input("Enter a number: "))
product = product_of_digits(number)
print("Product of digits:", product)