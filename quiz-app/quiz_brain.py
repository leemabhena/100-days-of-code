

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        reply = input(f"Q.{self.question_number}: {item.text}. (True / False):  ")
        self.check_answer(item.answer, reply)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right")
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print('That was wrong')
            print(f"Your current score is {self.score}/{self.question_number}")
        print(f'The correct answer is {correct_answer}')
        print("\n")





