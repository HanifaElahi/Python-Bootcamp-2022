# Imports
from turtle import Turtle

# Declaring CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Creating Snake class
class Snake:

    # Initializing Constructor
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

     # Method for creating snakes
    def create_snake(self):
        #Creating 3 segments
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white") # setting color
            new_segment.penup() # using pendown so that line couldn't be drawn
            new_segment.goto(position) # moving segments to their destined position
            self.segments.append(new_segment)

    def move(self):
        # Logic : Move 3rd segment to 2nd segment position and 2nd segment to 1st segment position
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Moving first segment forward
        self.head.forward(MOVE_DISTANCE)
    
    # If snake is not facing downwards then move its head to upwards
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

     # If snake is not facing upwards then move its head to downwards
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    # If snake is not facing right then move its head to left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # If snake is not facing left then move its head to right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
