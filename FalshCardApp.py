#Flashcard App
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Q: {self.question}\nA: {self.answer}\n"

class FlashcardApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)

    def start(self):
        print("Welcome to the Flashcard App!")
        print("Enter 'q' to quit.")

        while True:
            random_flashcard = random.choice(self.flashcards)
            print(random_flashcard.question)

            user_input = input("Press enter to reveal the answer or 'q' to quit: ")

            if user_input == 'q':
                break

            print(random_flashcard.answer)

def main():
    flashcard_app = FlashcardApp()

    # Create flashcards
    flashcard1 = Flashcard("What is the capital of France?", "Paris")
    flashcard2 = Flashcard("Who painted the Mona Lisa?", "Leonardo da Vinci")
    flashcard3 = Flashcard("What is the largest planet in our solar system?", "Jupiter")

    # Add flashcards to the app
    flashcard_app.add_flashcard(flashcard1)
    flashcard_app.add_flashcard(flashcard2)
    flashcard_app.add_flashcard(flashcard3)

    # Start the flashcard app
    flashcard_app.start()

main()