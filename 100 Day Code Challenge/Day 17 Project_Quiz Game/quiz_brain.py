class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def question_remaning(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_response = input(f"Q{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(user_response, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You got it Right!")
        else:
            print("Thats Wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

