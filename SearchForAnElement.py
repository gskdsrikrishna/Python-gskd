#28.Search for an element in an array
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
numbers = [5, 2, 8, 12, 1, 9]
print(numbers)
target = int(input("Enter the number:"))
index = linear_search(numbers, target)
if index != -1:
    print("Element", target, "found at index", index)
else:
    print("Element", target, "not found in the array.")