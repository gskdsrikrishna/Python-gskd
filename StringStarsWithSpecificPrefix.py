#87.Check if a stirng starts with a specific prefix
string = input("Enter a string: ")
prefix = input("Enter a prefix: ")

if string.startswith(prefix):
    print("The string starts with the prefix.")
else:
    print("The string does not start with the prefix.")