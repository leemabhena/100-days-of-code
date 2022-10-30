from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(q['text'], q['answer']) for q in question_data]

qns = QuizBrain(question_bank)

while qns.still_has_questions():
    qns.next_question()


print("You have completed the quiz.")
print(f"Your final score was {qns.score} / {qns.question_number}")