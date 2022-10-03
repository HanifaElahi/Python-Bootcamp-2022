import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = [
    "yellow", "deep pink", "red", "magenta", "lime", "dodger blue",
    "dark orange", "medium blue"
]

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(500):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))