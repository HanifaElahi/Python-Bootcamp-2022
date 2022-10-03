from turtle import Turtle


# In order to inherit all from Turtle

class Paddle(Turtle):
    # Initializing Paddle 
    def __init__(self, position):
        super().__init__() # Inheriting Turtle class
        self.shape("square") # Setting shape
        self.color("white") # setting color
        self.shapesize(stretch_wid=5, stretch_len=1) # setting shape
        self.penup() # penup so that there could be no trace
        self.goto(position) # Specifying Position of paddles
    
    # In order to move Paddle Up
    
    def go_up(self): 
        new_y = self.ycor() + 20 # adding in existing co-ordinate
        self.goto(self.xcor(), new_y)
    
    # In order to move Paddle Down
    
    def go_down(self):
        new_y = self.ycor() - 20 # subtracting in existing co-ordinate
        self.goto(self.xcor(), new_y)