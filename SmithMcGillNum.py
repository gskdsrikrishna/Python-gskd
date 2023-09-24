#75.Check if a number is a Smith McGill number
def is_smith_mcgill_number(number):
    sum_of_digits = sum(int(digit) for digit in str(number))
    sum_of_prime_factors = sum(prime_factors(number))
    return sum_of_digits == sum_of_prime_factors

def prime_factors(number):
    factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

# Example usage:
number = int(input("Enter a number: "))
if is_smith_mcgill_number(number):
    print(number, "is a Smith McGill number.")
else:
    print(number, "is not a Smith McGill number.")