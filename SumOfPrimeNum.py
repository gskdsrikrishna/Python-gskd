#50.Calculate the sum of all prime numbers up to a given list
limit = int(input("Enter the limit: "))

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

prime_sum = 0
for num in range(2, limit + 1):
    if is_prime(num):
        prime_sum += num

print("Sum of prime numbers up to", limit, "is", prime_sum)