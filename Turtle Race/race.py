from turtle import Turtle , Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title= "Make Your Bet", prompt= "Which Turtle will win the race ?\nEnter a color:")
r = Turtle()
r.color("red")
g = Turtle()
g.color("green")
b = Turtle()
b.color("blue")
v = Turtle()
v.color("violet")
o = Turtle()
o.color("orange")
p = Turtle()
p.color("purple")
letters = [r , g , b ,v , o , p ]
y = -150
for letter in letters:
    x = -230
    letter.penup()
    letter.shape("turtle")
    letter.goto(x,y)
    y += 60
    letter.pendown()

if user_bet:
    is_race_on = True

while  is_race_on :
    for letter in letters:
        if letter.xcor() > 230:
            is_race_on = False
            winning_color = letter.pencolor()
            if winning_color == user_bet:
                print(f"You'ev Won ! the {winning_color} Turtle is the Winner!!")
                break
            else:
                print(f"You'ev Lost ! the {winning_color} Turtle is the Winner!!")
                break

        rand_distance = random.randint(0,10)
        letter.forward(rand_distance)

screen.exitonclick()
