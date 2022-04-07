# step 1 import data
import pandas as pd
import turtle

# step 2 construct objects

screen = turtle.Screen()

screen.title("U.S.States.Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.Turtle(image)

## step 3 read data from file

data = pd.read_csv("50_states.csv")


# step 4 ask the user for an input


all_states = data.state.to_list()


guessed_states = []

while len(guessed_states) < 50:
    user_state = screen.textinput(title=f"{len(guessed_states)}/50 from states", prompt="what is your state").title()

    if user_state == "Exit":
        new_data = [state for state in all_states if state not in guessed_states]

        learn_states = pd.DataFrame(new_data)
        learn_states.to_csv("learn_missing_states.csv")

        break

    if user_state in all_states:

        if user_state not in guessed_states:
            guessed_states.append(user_state)

            state_data = data[data.state == user_state]

            tom = turtle.Turtle()
            tom.hideturtle()
            tom.penup()
            tom.goto(int(state_data.x), int(state_data.y))
            tom.write(user_state)











