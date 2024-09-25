class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.score = 0
        self.question_list = list

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q:{self.question_number} {curr_question.text} (True/False): ")
        self.check_answer(user_answer, curr_question.answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, curr_answer):
        if user_answer.lower() == curr_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {curr_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
