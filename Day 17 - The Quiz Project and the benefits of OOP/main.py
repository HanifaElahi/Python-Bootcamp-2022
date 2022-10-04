# Imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Taking questions list
question_bank = []

# Iterating over questions data
for question in question_data:
    # Fetching Question
    question_text = question["question"]
    # Fetching Answer
    question_answer = question["correct_answer"]
     # Creating new question
    new_question = Question(question_text, question_answer)
    # Appending in question bank
    question_bank.append(new_question)

# Creating object
quiz = QuizBrain(question_bank)

# Ask questions until all questions are asked
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")