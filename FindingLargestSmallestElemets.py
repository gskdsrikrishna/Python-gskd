#49.Find the largest and smallest numbers in an array
# Initialize an empty array
numbers = []

# Take input for the size of the array
size = int(input("Enter the size of the array: "))

# Take input for each element of the array
for i in range(size):
    element = int(input("Enter element at index {}: ".format(i)))
    numbers.append(element)

# Print the array elements
print("Array elements:", numbers)

# Find the largest number in the array
largest = max(numbers)
print("Largest number:", largest)

# Find the smallest number in the array
smallest = min(numbers)
print("Smallest number:", smallest)

# Sort the array in ascending order
sorted_array = sorted(numbers)
print("Sorted array:", sorted_array)