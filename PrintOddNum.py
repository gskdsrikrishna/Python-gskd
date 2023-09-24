#99.Print odd numbers
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

odd_numbers = [num for num in range(start, end+1) if num % 2 != 0]
print("Odd numbers:", odd_numbers)