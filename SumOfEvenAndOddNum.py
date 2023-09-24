#64.Find the sum of all even and odd numbers
def sum_of_even_or_odd_numbers(number_list, even=True):
    result = 0
    for number in number_list:
        if number % 2 == 0 and even:
            result += number
        elif number % 2 != 0 and not even:
            result += number
    return result

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_sum = sum_of_even_or_odd_numbers(numbers, even=True)
odd_sum = sum_of_even_or_odd_numbers(numbers, even=False)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)