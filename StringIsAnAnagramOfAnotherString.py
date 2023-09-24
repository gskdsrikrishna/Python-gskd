#38.Check if a string is an angram of another string
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")