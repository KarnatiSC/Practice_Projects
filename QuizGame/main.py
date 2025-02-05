from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = Quizbrain(question_bank)

is_correct = True

while quiz.if_quiz_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")






