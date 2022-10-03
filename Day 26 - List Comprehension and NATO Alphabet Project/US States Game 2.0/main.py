# Imports
import turtle
import pandas

screen = turtle.Screen() # Initializing Screen object
screen.title("U.S. States Game") # Setting Screen Title
image = "blank_states_img.gif"
screen.addshape(image) # Adding image on screen
turtle.shape(image) # Setting Turtle shape as of image

data = pandas.read_csv("50_states.csv") # Reading csv 
all_states = data.state.to_list() # Taking states into list
guessed_states = []

while len(guessed_states) < 50:
    
    # Pop-up box
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title() # converting to title case
    
    # If exit is entered in the pop up box
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states] 
        new_data = pandas.DataFrame(missing_states) # Loading into DataFrame
        new_data.to_csv("states_to_learn.csv") # Exporting to csv
        break
    
    # If state name entered is in all states list
    if answer_state in all_states:
        guessed_states.append(answer_state) # Append in guessed states list
        t = turtle.Turtle() # create turtle
        t.hideturtle() # hide turtle
        t.penup() # penup so that there could be no trace
        state_data = data[data.state == answer_state] # fetch the row of matched state
        t.goto(int(state_data.x), int(state_data.y)) # Goto state's x-coordinate and y-coordinate
        t.write(answer_state)# write in desired position
