from turtle import Turtle


class Scoreboard(Turtle):
    
    # Initializing Turtle
    def __init__(self):
        super().__init__() # Inheriting everything from turtle class
        self.color("white") # setting color
        self.penup() # penup so that there could be no trace
        self.hideturtle() # hiding up the turtle
        self.l_score = 0 # initializing left score
        self.r_score = 0 # initializing right score
        self.update_scoreboard() # update scoreboard method
       
    # Method for updating score board
    
    def update_scoreboard(self):
        self.clear()
        # Write left side score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # Write Rightt side score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    
    # Assigning Point to Left 
    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    # Assigning Point to Right
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()