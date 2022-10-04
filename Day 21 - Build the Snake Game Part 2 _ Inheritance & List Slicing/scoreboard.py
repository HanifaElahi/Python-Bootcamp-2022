# Imports
from turtle import Turtle

# Declaring CONSTANTS
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Creating Scoreboard class
class Scoreboard(Turtle):

    # Initializing Constructor
    def __init__(self):
        super().__init__() # Inheriting everythin from super class
        self.score = 0 # setting initial score
        self.color("white") # setting color
        self.penup() # penup so that there could be no trace
        self.goto(0, 270) # setting scoreboard position
        self.hideturtle() # hiding turtle
        self.update_scoreboard() # method for updating scoreboard

    # Method for updating scoreboard
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT) # write score

    # Method for game over condition
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Method for increasing score
    def increase_score(self):
        self.score += 1 # Increment score
        self.clear() 
        self.update_scoreboard() # Update the scoreboard in case of increasing score