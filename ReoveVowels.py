#92.Remove all vowels in a string
string = input("Enter a string: ")

vowels = "aeiouAEIOU"
string_without_vowels = "".join(char for char in string if char not in vowels)
print("String without vowels:", string_without_vowels)