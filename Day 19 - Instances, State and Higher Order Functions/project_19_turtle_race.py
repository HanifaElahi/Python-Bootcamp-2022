# Imports
import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400) # setting height and width of the window

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") # for taking text input

colors = ["red", "orange", "yellow", "lime", "blue", "purple", "deep pink", "brown"] # Specifying turtle colors

y_positions = [-100,-70,-40, -10, 20, 50, 80, 110] # describing y co-ordinates as x will be same(starting point)

all_turtles = []

# Creating 8 Turtles
for i in range(0,8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

# If user has made the bet then start the race
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            
            is_race_on = False
            
            winning_color = turtle.pencolor() # Getting the pen color of winning turtle
            
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!") 
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
             
        rand_distance = random.randint(0, 10) # Generating Random Distance
        turtle.forward(rand_distance) # Each turtle will move forward with random distance

screen.exitonclick()