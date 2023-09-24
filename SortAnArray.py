#27.Sort an array of integers
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
numbers = [5, 2, 8, 12, 1, 9]
bubble_sort(numbers)
print("Sorted array:", numbers)