#37.Find the average of all elements in an array
numbers = [5, 2, 8, 12, 1, 9]
sum_of_array = 0

for num in numbers:
    sum_of_array += num

average = sum_of_array / len(numbers)
print("Average of array elements:", average)