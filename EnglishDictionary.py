#English Dictionary
from nltk.corpus import wordnet

def search_word(word):
    synsets = wordnet.synsets(word)

    if synsets:
        print(f"Definitions of '{word}':")
        for synset in synsets:
            print(f"- {synset.definition()}")

        synonyms = []
        for synset in synsets:
            for lemma in synset.lemmas():
                synonyms.append(lemma.name())

        print(f"\nSynonyms of '{word}':")
        if synonyms:
            print(", ".join(synonyms))
        else:
            print("No synonyms found.")
    else:
        print(f"No definitions found for '{word}'.")

def main():
    while True:
        print("\nEnglish Dictionary")
        print("1. Search for a word")
        print("2. Quit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            word = input("Enter a word: ")
            search_word(word)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()