# Necessay Imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen() # Screen object
screen.setup(width=600, height=600) # set screen width and sreen height
screen.bgcolor("black") # set screen color
screen.title("My Snake Game") # set screen title
screen.tracer(0) # keeping tracer off

snake = Snake() # Snake object
food = Food() # Food object
scoreboard = Scoreboard() # Scoreboard object

# Setting up screen event listeners
screen.listen()
screen.onkey(snake.up, "Up") # Move snake up with Up key
screen.onkey(snake.down, "Down") # Move snake down with Down key
screen.onkey(snake.left, "Left") # Move Left up with left key
screen.onkey(snake.right, "Right") # Move snake right with Right key

game_is_on = True

while game_is_on:
    
    screen.update() # Update screen 
    time.sleep(0.1) 
    snake.move() # Move snake

    # Detect collision with food.
    if snake.head.distance(food) < 15: # If collision occurs
        food.refresh() # Refresh food on new position
        snake.extend() # Increase snake size
        scoreboard.increase_score() # Increase Score

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False # Game over in case of wall collision
        scoreboard.reset() # Reset Scoreboard

    #Detect collision with tail.
    for segment in snake.segments: 
        if segment == snake.head: 
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset() # Reset Scoreboard

screen.exitonclick()
