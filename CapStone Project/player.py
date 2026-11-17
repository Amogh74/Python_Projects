from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 290


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_strt()
        self.setheading(90)

    def goto_strt(self):
        self.goto(STARTING_POSITION)

    def Move(self) :
        self.forward(MOVE_DISTANCE)

    def finished_race(self):
       return self.ycor() >FINISH_LINE_Y
