#35.Find the frequency of each element in the array
def find_element_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

# Example usage:
array = [5, 2, 8, 12, 1, 9, 5, 2, 2]
element_frequency = find_element_frequency(array)
print("Element frequency:", element_frequency)