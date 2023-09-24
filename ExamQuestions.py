import random

class ExamQuestion:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Exam:
    def __init__(self, questions):
        self.questions = questions

    def generate_exam(self):
        random.shuffle(self.questions)
        for idx, question in enumerate(self.questions, start=1):
            print(f"Question {idx}: {question.question}")
            for choice_idx, choice in enumerate(question.choices, start=1):
                print(f"{choice_idx}. {choice}")
            user_answer = input("Enter your answer (1-{}): ".format(len(question.choices)))
            if question.check_answer(user_answer):
                print("Correct!\n")
            else:
                print("Incorrect!\n")

def main():
    # Sample questions for the exam
    question1 = ExamQuestion("What is the capital of France?", ["A. Paris", "B. London", "C. Rome", "D. Madrid"], "A")
    question2 = ExamQuestion("What is the largest planet in our solar system?", ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"], "C")
    question3 = ExamQuestion("Who painted the Mona Lisa?", ["A. Michelangelo", "B. Leonardo da Vinci", "C. Vincent van Gogh", "D. Pablo Picasso"], "B")
    question4 = ExamQuestion("What is the symbol for the chemical element iron?", ["A. Fe", "B. Au", "C. Ag", "D. Hg"], "A")
    question5 = ExamQuestion("What is the powerhouse of the cell?", ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Golgi Apparatus"], "B")

    # Create an exam with the questions
    exam = Exam([question1, question2, question3, question4, question5])

    # Generate the practice exam
    exam.generate_exam()


if __name__ == "__main__":
    main()