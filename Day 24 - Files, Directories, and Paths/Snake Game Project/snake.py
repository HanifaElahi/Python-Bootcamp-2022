# Imports
from turtle import Turtle

# Declaring CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Creating Snake Class
class Snake:

    # Declaring Constructor
    def __init__(self):
        self.segments = [] # segments list
        self.create_snake() # create snake method
        self.head = self.segments[0] # setting head as first segment
    
    # Method for creating Snake -- create snake using 3 segments placed on starting positions each of 20 pixels
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position) # Add segment on each position

    # Method for creating segments -- 
    def add_segment(self, position):
        new_segment = Turtle("square") # Setting shape
        new_segment.color("white") # Setting color
        new_segment.penup() # penup for no trace
        new_segment.goto(position) # Moving Segment to position 
        self.segments.append(new_segment) # Appending segments to list

    # Extending Snake Segment -- Add new segment to last position
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Method for Snake Movement 
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Setting Direction Upwards -- only if head is not facing down
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    # Setting Direction Downwards -- only if head is not facing upwards
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    # Setting Direction Left -- only if head is not facing right
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Setting Direction Right -- only if head is not facing left
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
