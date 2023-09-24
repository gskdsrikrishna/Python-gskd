#52.Reverse the order of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = " ".join(reversed(words))
print("Reversed sentence:", reversed_sentence)