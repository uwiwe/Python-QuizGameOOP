from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
user_playing = True

for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

for question in range(0, len(question_bank)):
    quiz.next_question()
print("End of the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
