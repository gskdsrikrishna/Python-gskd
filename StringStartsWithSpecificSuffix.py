#88.Check if a string ends with a specific suffix
string = input("Enter a string: ")
suffix = input("Enter a suffix: ")

if string.endswith(suffix):
    print("The string ends with the suffix.")
else:
    print("The string does not end with the suffix.")