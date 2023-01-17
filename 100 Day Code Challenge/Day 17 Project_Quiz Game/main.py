from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
length = len(question_data)

for i in range(length):
    text = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.question_remaning():
    quiz.next_question()

print("Congratulations! You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
