#79.Check if a chracter is a uppercase/lowercase
character = input("Enter a character: ")
if character.isupper():
    print(character, "is an uppercase character.")
elif character.islower():
    print(character, "is a lowercase character.")
else:
    print(character, "is not an uppercase or lowercase character.")