from turtle import Turtle


class Ball(Turtle):
    # Initializing Constructor
    def __init__(self):
        super().__init__() # Inheriting everything from turtle class
        self.color("white") # setting color
        self.shape("circle") # setting shape
        self.penup() # penup so that there could be no trace
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    # For changing Direction upon collision with wall
    def bounce_y(self):
        self.y_move *= -1 # If collision occurs then move in reverse
    
    #Detect collision with paddle
    def bounce_x(self): 
        self.x_move *= -1 # If collision occurs then move in reverse
        self.move_speed *= 0.9 # setting speed after collision i.e faster than before

    # Method for Rsetting position
    def reset_position(self):
        self.goto(0, 0) # go to origin
        self.move_speed = 0.1 # setting move speed
        self.bounce_x() # to reverse direction
