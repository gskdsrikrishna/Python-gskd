#33.Check if a number is perfect number
number = int(input("Enter a number: "))
divisor_sum = 0

for divisor in range(1, number):
    if number % divisor == 0:
        divisor_sum += divisor

if divisor_sum == number:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")