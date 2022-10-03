# Imports
import random
from turtle import Turtle

# Declaring CONSTANTS
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    # Initializing Constructor
    def __init__(self):
        self.all_cars = [] 
        self.car_speed = STARTING_MOVE_DISTANCE # setting initial car speed as 5

    def create_car(self):
        random_chance = random.randint(1, 6) # if random chance is equal to 1 only then create car --- in order to stop greater number of cars being created
        if random_chance == 1:
            new_car = Turtle("square") # car of square shape 
            new_car.shapesize(stretch_wid=1, stretch_len=2) 
            new_car.penup() # so that path gets invisible
            new_car.color(random.choice(COLORS)) # random color
            random_y = random.randint(-250, 250) # setting random position - good range in the middle of the screen
            new_car.goto(300, random_y) # x - very edge of the screen , y - random
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed) 

    # Method for levelling up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT # increasing speed
