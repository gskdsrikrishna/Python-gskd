#98.Print even numbers
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

even_numbers = [num for num in range(start, end+1) if num % 2 == 0]
print("Even numbers:", even_numbers)