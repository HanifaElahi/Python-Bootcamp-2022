# Imports
from turtle import Turtle

# Declaring CONSTANTS
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Creating Scoreboard Class
class Scoreboard(Turtle):

    # Initializing Constructor
    def __init__(self):
        super().__init__() # Inheritance
        self.score = 0 # setting initial score
        # Reading Previous High Score from data.txt
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white") # Setting color for turtle
        self.penup() # Penup for no trace
        self.goto(0, 270) # Goto coordinates (0,270)
        self.hideturtle() # Hiding turtle
        self.update_scoreboard() # Update Scoreboard Method

    # Method for Updating Scoreboard
    def update_scoreboard(self):
        self.clear() # clear it first
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # Method for Resetting Score
    def reset(self):
        # if current score is grater than previous high score
        if self.score > self.high_score:
            self.high_score = self.score # Set current score as high score
            # For writing Highest Score far by now in data.txt
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")  # Write high score in file
        self.score = 0 # Setting Score again to 0
        self.update_scoreboard() # Update Scoreboard

    # Method for Increasing Scoreboard
    def increase_score(self):
        self.score += 1 # Increment in Score
        self.update_scoreboard() # Update score
