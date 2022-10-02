# Imports
from turtle import Turtle
import random

# Creating food Class
class Food(Turtle):
    
    # Initializing Constructor
    def __init__(self):
        super().__init__() # Inheritance --> inherit everything from Turtle class
        self.shape("circle") # specifying shape
        self.penup() # using penup so that no trace could be drawn
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Setting shapesize as we want rectanguar/shape shape
        self.color("blue") # specifying color
        self.speed("fastest") # setting speed
        self.refresh() 

    # Function for Food Refresh 
    def refresh(self):
        random_x = random.randint(-280, 280) # Generate random x-coordinate between -280 and 280
        random_y = random.randint(-280, 280) # Generate random y-coordinate between -280 and 280
        self.goto(random_x, random_y) # Moving food to randomly generated positions
