import random
import turtle as turtle_module
#TODO : 10X10 painting , each dot 20 in size and spaced apart by 50
screen = turtle_module.Screen()
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.shape("arrow")
tim.speed("fast")
colour_list =[ (136, 164, 198), (220, 153, 106), (30, 42, 61), (200, 136, 147), (157, 63, 53), (234, 212, 94), (50, 101, 141),
               (138, 180, 162), (146, 64, 72), (165, 28, 34), (156, 32, 27), (52, 42, 44), (53, 46, 43), (61, 114, 99),
               (230, 164, 170), (233, 168, 160), (209, 85, 75), (33, 59, 53), (18, 93, 69), (173, 188, 219), (195, 98, 106),
               (34, 60, 104), (108, 125, 160), (174, 201, 191), (21, 80, 100), (40, 150, 205)]
tim.setheading(225)
tim.penup()## no need for pen down as dots dont need pen
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(colour_list))
    tim.forward(50)

    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen.exitonclick()
