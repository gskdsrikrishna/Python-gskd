#51.Find the frequency of each word in a text file
from collections import defaultdict

# Open the text file
with open("C:/Users/GS.Devarayulu/OneDrive/Desktop/100 Programs.txt", "r") as file:
    word_count = defaultdict(int)

    # Read each line and split into words
    for line in file:
        words = line.strip().split()
        for word in words:
            word_count[word] += 1

    # Print the frequency of each word
    for word, count in word_count.items():
        print(word, ":", count)