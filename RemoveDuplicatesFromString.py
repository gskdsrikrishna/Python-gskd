#90.Remove duplicate characters from a string
string = input("Enter a string: ")

unique_chars = "".join(set(string))
print("String with duplicate characters removed:", unique_chars)