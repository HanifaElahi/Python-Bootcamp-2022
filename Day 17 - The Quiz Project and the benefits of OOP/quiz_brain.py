# Creating Class

class QuizBrain:
    
    # Initializing Constructor
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    # Method for checking if questions are still there or not
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    # Method for moving to next question
    def next_question(self):
        current_question = self.question_list[self.question_number] # Get the current question number
        self.question_number += 1 # Increment 
        # Ask user for answer
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )
        # Calling check answer method
        self.check_answer(user_answer, current_question.answer)
    
    # Method for checking answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower(): # If actual answer and user answer are same
            self.score += 1 # Increment score
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
