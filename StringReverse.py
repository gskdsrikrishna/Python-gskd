#32.Reverse a string
def reverse_string(string):
    return string[::-1]

# Example usage:
text = input("Enter a string: ")
reversed_text = reverse_string(text)
print("Reversed string:", reversed_text)