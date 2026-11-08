from turtle import Turtle ,Screen
screen = Screen()
t = Turtle()
t.shape("turtle")
t.speed("fast")
t.pensize(4)
i = 10
j = -10
def move_forward():
    t.forward(20)

def move_back():
    t.back(20)

def anti_clockwise():
    new = t.heading() + 10
    t.setheading(new)

def clockwise():
    new =t.heading() - 10
    t.setheading(new)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key ="w",fun =move_forward)
screen.onkey(key ="s",fun = move_back )
screen.onkey(key ="d",fun = clockwise )
screen.onkey(key ="a",fun = anti_clockwise )
screen.onkey(key ="v",fun = clear )
#Higher Order Functions are functions that take other functions as input.
screen.exitonclick()
