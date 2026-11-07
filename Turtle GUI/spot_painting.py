# we use colorgram to extact colour from a jpg image . Read the Documentation for more context
# import colorgram
# colors = colorgram.extract('images.jpg',30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r , g ,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen
#TODO : 10X10 painting , each dot 20 in size and spaced apart by 50
screen = Screen()
turtle.colormode(255)
tim = Turtle()
tim.shape("arrow")
colour_list =[ (136, 164, 198), (220, 153, 106), (30, 42, 61), (200, 136, 147), (157, 63, 53), (234, 212, 94), (50, 101, 141),
               (138, 180, 162), (146, 64, 72), (165, 28, 34), (156, 32, 27), (52, 42, 44), (53, 46, 43), (61, 114, 99),
               (230, 164, 170), (233, 168, 160), (209, 85, 75), (33, 59, 53), (18, 93, 69), (173, 188, 219), (195, 98, 106),
               (34, 60, 104), (108, 125, 160), (174, 201, 191), (21, 80, 100), (40, 150, 205)]
tim.penup()# no need of pendown() as dot draws regardless
tim.hideturtle()
x = -220
y = -220
tim.goto(x,y)
for i in range(10):
    for j in range(10):
        tim.color(random.choice(colour_list))
        tim.dot(20)
        tim.forward(50)

    y += 50
    tim.goto(x ,y)

screen.exitonclick()
