# Imports
from turtle import Turtle

# Declaring Constants
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    # Initializing Constructor
    def __init__(self):
        super().__init__() # Inheriting everything from Turtle class
        self.level = 1 # setting initial level
        self.hideturtle() # hiding turtle
        self.penup() # penup so that there could be no trace
        self.goto(-280, 250) # setting scoreboar position
        self.update_scoreboard() # method for updating scoreboard

    # MEthod for updating scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Method for increasing Level
    def increase_level(self):
        self.level += 1 # increase level by 1
        self.update_scoreboard() # update scoreboard

    # Method for game over condition
    def game_over(self):
        self.goto(0, 0) # moving back to origin
        self.write(f"GAME OVER", align="center", font=FONT)