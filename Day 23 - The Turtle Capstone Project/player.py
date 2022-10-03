# Imports
from turtle import Turtle

# Declaring Costants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    # Initializing Constructor
    def __init__(self):
        super().__init__() # Inherit everything from turtle class
        self.shape("turtle")
        self.penup() # just remain in shape and doesn't draw
        self.go_to_start() # move to starting position
        self.setheading(90) # setting heading which north i.e 90 degrees

    def go_up(self):
        self.forward(MOVE_DISTANCE) #go up by 10 pixels

    def go_to_start(self):
        self.goto(STARTING_POSITION) # go to starting position

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y: # if y co-ordinate is greater than 280 
            return True
        else:
            return False
