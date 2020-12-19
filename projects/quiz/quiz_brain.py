class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self, question_list):
        number_of_questions = len(self.question_list)
        return self.question_number < number_of_questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.question} (True/False)?: ")
