#Hangman
import random

def select_word():
    word_list = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grapefruit",
                 "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange",
                 "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    return random.choice(word_list)

def initialize_game():
    word = select_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6
    return word, guessed_letters, incorrect_guesses, max_guesses

def display_hangman(incorrect_guesses):
    hangman = [
        """
        +---+
            |
            |
            |
           ===
        """,
        """
        +---+
        O   |
            |
            |
           ===
        """,
        """
        +---+
        O   |
        |   |
            |
           ===
        """,
        """
        +---+
        O   |
       /|   |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\  |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\  |
       /    |
           ===
        """,
        """
        +---+
        O   |
       /|\  |
       / \  |
           ===
        """
    ]
    print(hangman[incorrect_guesses])

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    print(displayed_word)

def get_player_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
        elif not guess.isalpha():
            print("Invalid input. Please enter a letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        else:
            return guess

def play_game():
    word, guessed_letters, incorrect_guesses, max_guesses = initialize_game()

    print("Welcome to Hangman!")
    display_word(word, guessed_letters)

    while True:
        guess = get_player_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            display_word(word, guessed_letters)
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
            display_hangman(incorrect_guesses)
            display_word(word, guessed_letters)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word correctly!")
            break

        if incorrect_guesses == max_guesses:
            print("Game over! You ran out of guesses.")
            print(f"The word was: {word}")
            break

play_game()