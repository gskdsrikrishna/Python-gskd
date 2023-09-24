#31.Find the second highest number in an array
def find_second_highest(numbers):
    highest = float('-inf')
    second_highest = float('-inf')

    for num in numbers:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num

    return second_highest

# Example usage:
array = [5, 2, 8, 12, 1, 9]
print(array)
second_highest = find_second_highest(array)
print("Second highest number:", second_highest)