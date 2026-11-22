import turtle
import pandas as pd
#turtle only works with gif
screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(750,550)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
Writer = turtle.Turtle()
# def get_mouse_click_coor(x,y):
#     print(x,y)  , we have the data now
# turtle.onscreenclick(get_mouse_click_coor)
#TODO: Write ans at correct location if correct , keep progress in heading
data = pd.read_csv("50_states.csv")
US_states = data["state"].to_numpy()#converts into a numpy array
ans_guessed = []
ans_correct = 0
while len(ans_guessed) <50 :
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    answer_state = screen.textinput(title=f"{ans_correct}/50 Correct",prompt="What's Another State's name?").capitalize()
    if len(ans_guessed) == len(US_states):
        t.goto(0,0)
        t.write("Congrats , You Guessed Every State .Game Over!!")
    if answer_state == "Exit":
        not_guessed = []
        for states in US_states:
            if states not in ans_guessed:
                not_guessed.append(states)

        new_data = pd.DataFrame(not_guessed)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in US_states:
        ans_correct += 1
        ans_guessed.append(answer_state)
        # x_cor = data.loc[data.state == f"{answer_state}", "x"].iloc[0]
        # y_cor = data.loc[data.state == f"{answer_state}", "y"].iloc[0]
        # writing_Turtle.move(x_cor,y_cor)
        # writing_Turtle.write(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())#can get a particular value of a table without index and other bs
        t.write(answer_state)

#To make states to learn_csv

turtle.mainloop()#alternative way to keep our screen open even though code is finished executing