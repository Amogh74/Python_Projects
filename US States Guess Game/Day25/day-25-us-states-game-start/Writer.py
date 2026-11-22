from turtle import Turtle

class write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move(self,a , b):
        self.goto(a,b)

    def WRITE(self,str):
        self.write(str)