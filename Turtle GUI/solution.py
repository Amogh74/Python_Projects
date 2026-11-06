#Random Walk
import turtle as t
from turtle import Screen
import random

from prompt_toolkit.layout import screen

from colour import colors_list
screen = Screen()
tim = t.Turtle()
tim.shape("turtle")
# colours = colors_list
directions = [0 , 90 , 180, 270]
# tim.pensize(10)
tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colors_list))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



#Random Color choosing instead of picking a random color from the list we created
#Tuple is used , Syntax => a = (1,2,3) , Tuple is immutable
# R G B ranges from 1.0 to 255 individually hence mixing 32R , 12G , 255B will give a unique color
#https://www.w3schools.com/colors/colors_rgb.asp --> interactive link
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return  color



# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


#Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        currernt_heading = tim.heading()
        tim.setheading(currernt_heading +size_of_gap)
        tim.circle(100)

draw_spirograph(5)
screen.exitonclick()
