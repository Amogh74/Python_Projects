from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.Segments = []
        self.create_snake()
        self.head = self.Segments[0]


    def create_snake(self):
        for position in STARTING_POSITION :
            self.add_Segment(position)


    def move(self):
        for turt_num in range(len(self.Segments) - 1, 0, -1):  # range(start=  2, stop= 0 ,step= -1)
            new_x = self.Segments[turt_num - 1].xcor()  # Second turtle
            new_y = self.Segments[turt_num - 1].ycor()  # Second turtle
            self.Segments[turt_num].goto(new_x, new_y)  # Last Turtle
        self.Segments[0].forward(MOVE_DISTANCE)


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

    def add_Segment(self,position):
        new_Segment = Turtle("square")
        new_Segment.color("white")
        new_Segment.penup()
        new_Segment.goto(position)
        self.Segments.append(new_Segment)

    def extend(self):
        #add new segment to the snake
        self.add_Segment(self.Segments[-1].position() )#Last Segment of the snake
