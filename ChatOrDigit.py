#82.Check if a character is a character or digit
character = input("Enter a character: ")
if character.isalpha():
    print(character, "is a letter.")
elif character.isdigit():
    print(character, "is a digit.")
else:
    print(character, "is neither a letter nor a digit.")