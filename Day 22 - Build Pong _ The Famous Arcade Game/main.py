#Importing Libraries
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# Creating Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) # To turn off the animation

# Initializing Left and Right Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Control Paddle with Keys
screen.listen()
# Right Paddle Movement
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Left Paddle Movement
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Initializing Ball
ball = Ball()

game_is_on = True

while game_is_on:
    
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position() # resetting position
        scoreboard.l_point() # give point to left when right paddle misses

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position() # resetting position
        scoreboard.r_point() # give point to right when left paddle misses

screen.exitonclick()