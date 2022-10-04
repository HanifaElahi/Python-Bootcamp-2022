# Imports
import random
from turtle import Turtle

# Creating Food class
class Food(Turtle):
    
    # Initializing Constructor
    def __init__(self):
        super().__init__() # Inheriting everythin that Turtle super class has
        self.shape("circle") # Setting shape
        self.penup() # penup so that there is no trace
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5) # setting shape size
        self.color("blue") # setting color
        self.speed("fastest") # setting speed
        self.refresh() # refresh method
    
    # Method for Food refresh
    def refresh(self):
        random_x = random.randint(-280,280) # Generating random x-coordinate
        random_y = random.randint(-280,280) # Generating random y-coordinate
        self.goto(random_x, random_y) # Move to this position
            
        