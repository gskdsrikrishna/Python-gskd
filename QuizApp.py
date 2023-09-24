#Quiz Application
def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz!")
    print("Answer the following questions:")

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, option in enumerate(question['options'], start=1):
            print(f"{j}. {option}")

        while True:
            user_answer = input("Enter your answer (1-4): ")

            if user_answer not in ['1', '2', '3', '4']:
                print("Invalid input. Please enter a valid option.")
            else:
                break

        user_answer = int(user_answer)
        correct_answer = question['answer']

        if user_answer == correct_answer:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer!")

        print(f"The correct answer is: {question['options'][correct_answer-1]}")

    print("\nQuiz completed!")
    print(f"You scored {score} out of {total_questions}.")

def main():
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Paris', 'Madrid', 'London', 'Rome'],
            'answer': 1
        },
        {
            'question': 'Who painted the Mona Lisa?',
            'options': ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh', 'Michelangelo'],
            'answer': 1
        },
        {
            'question': 'What is the largest planet in our solar system?',
            'options': ['Jupiter', 'Saturn', 'Earth', 'Mars'],
            'answer': 1
        }
        # Add more questions here
    ]

    run_quiz(questions)

main()