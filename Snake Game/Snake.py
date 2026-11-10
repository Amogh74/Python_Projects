from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]


    def create_snake(self):
        for position in STARTING_POSITION :
            new_Turtle = Turtle("square")
            new_Turtle.color("white")
            new_Turtle.penup()
            new_Turtle.goto(position)
            self.turtles.append(new_Turtle)

    def move(self):
        for turt_num in range(len(self.turtles) - 1, 0, -1):  # range(start=  2, stop= 0 ,step= -1)
            new_x = self.turtles[turt_num - 1].xcor()  # Second turtle
            new_y = self.turtles[turt_num - 1].ycor()  # Second turtle
            self.turtles[turt_num].goto(new_x, new_y)  # Last Turtle
        self.turtles[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
