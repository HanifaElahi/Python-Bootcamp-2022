#Importing Libraries
import time
from snake import Snake
from turtle import Turtle, Screen

#Setting up Screen Settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

###################################################### CREATING SNAKE ######################################################

snake = Snake()

###################################################### CONTROL SNAKE ######################################################

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

###################################################### MOVE SNAKE ########################################################

game_is_on = True

while game_is_on:
   
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()