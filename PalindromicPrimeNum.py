#72.Check if a number is a plaindromic prime
def is_palindromic_prime(number):
    return is_prime(number) and is_palindrome(number)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Example usage:
number = int(input("Enter a number: "))
if is_palindromic_prime(number):
    print(number, "is a palindromic prime number.")
else:
    print(number, "is not a palindromic prime number.")