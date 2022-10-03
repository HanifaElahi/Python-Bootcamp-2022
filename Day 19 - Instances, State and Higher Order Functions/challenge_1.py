from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    #tim.left(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    #tim.right(10)

def clear():
    tim.clear() #clear turtle drawings
    tim.penup() # penup so that no return path would be there
    tim.home() # bring turtle to middle or origin (0,0)
    tim.pendown() # making turtle again ready fpr drawing

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
