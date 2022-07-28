import turtle as tt
import pandas as pd

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()





screen = tt.Screen()
picture = "blank_states_img.gif"
screen.addshape(picture)
tt.shape(picture)
tt.title("State Game")
nota = 0
life = 0


is_on = True
while is_on:
    answer = screen.textinput(title= f"{nota}/50", prompt= "Introduce el name of the states").title()
    if answer == "Exit":
        break
    if answer in all_state:
        name = tt.Turtle()
        name.hideturtle()
        name.penup()
        new_state = data[data.state == answer]
        name.goto(int(new_state.x), int(new_state.y))
        name.write(answer)
        nota  +=1
    elif life == 5:
        life += 1
        name.write("you lose")
        break       
    





