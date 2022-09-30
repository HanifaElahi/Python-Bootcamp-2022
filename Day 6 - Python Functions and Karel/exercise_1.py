#move()
#move()
#move()
#turn_left()
#move()
#move()
#move()

# No turn_right() and turn_around() commands are there
# In order to turn around:

#turn_left()
#turn_left()

# In order to turn right:
#turn_left()
#turn_left()
#turn_left()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def make_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
make_square()
turn_right()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
