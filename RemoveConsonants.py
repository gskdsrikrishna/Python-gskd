#93.Remove all consonants from a string
string = input("Enter a string: ")

consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
string_without_consonants = "".join(char for char in string if char not in consonants)
print("String without consonants:", string_without_consonants)