#86.Extract sub string from a given string
string = input("Enter a string: ")
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

substring = string[start_index:end_index]
print("Extracted sub-string:", substring)