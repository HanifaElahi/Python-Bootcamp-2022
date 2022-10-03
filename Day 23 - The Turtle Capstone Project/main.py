# Imports
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initializing Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # turned off the tracer

# Creating obejcts
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# In order to screen to listen for events of key strokes
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    
    time.sleep(0.1) # update screen after 0.1 sec --  everything inside while loop will update after 0.1 sec
    screen.update()

    car_manager.create_car() # create cars till the game is on
    car_manager.move_cars() # move cars till the game is om

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            # game over condition
            game_is_on = False 
            scoreboard.game_over() 

    #Detect successful crossing
    if player.is_at_finish_line():
        # If players manages to cross finish line
        player.go_to_start() # Go to start
        car_manager.level_up() # level up
        scoreboard.increase_level() # Increase level on scoreboard
        
screen.exitonclick()