#implementing GUI concept Using Turtle GUI
from turtle import Turtle, Screen
import turtle as t
import random
from colour import colors_list


#from turtle import * --> this imports everything inside turtle and will behave like turtle exists in this file(not a good method)
#import turtle as t means we can write t wherever turtle is needed.
tim = Turtle()

screen = Screen()
tim.shape("turtle")
tim.speed("fastest")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# angle = [90 , 72 ,60 ,360/7.0 , 45, 40 , 36]
# loop = 4
# for i in angle:
#     tim.color(random.choice(colors_list))
#     for j in range(loop):
#         tim.forward(100)
#         tim.right(i)
#     loop +=1

#lambda is a way to create a small nameless functions , for example  add = lambda a, b: a+b , this is equal to:
#def add(a,b) :return a+b .
# walk = [lambda :tim.forward(30) ,
#         lambda :tim.right(90),
#         lambda :tim.left(90),
#         lambda :tim.forward(60),
#         lambda :tim.back(30),
#         lambda :tim.back(50),
#         lambda :tim.goto(0,11),
#         lambda :tim.goto(-10,-12),
#         lambda :tim.goto(5,6),
#         lambda :tim.goto(-5,6),
#         lambda :tim.home(),
#         lambda :tim.circle(20)
#         ]
#
# for _ in range(25):
#     tim.color(random.choice(colors_list))
#     random.choice(walk)()#First () will select a fxn and 2nd one will execute it

#Spirograph
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return  color

for _ in range(36):
    tim.color(random_color())
    tim.circle(100)
    tim.left(10)
    tim.circle(100)
screen.exitonclick()
