#83.Find the frequency of each character in a string
from collections import Counter

string = input("Enter a string: ")
character_count = Counter(string)

print("Character frequency:")
for character, count in character_count.items():
    print(character, ":", count)