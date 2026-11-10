from turtle import Screen , Turtle
import time
from Snake import Snake
#TODO 1: Create a Snake Body
#TODO 2: Move The Snake
#TODO 3: Create Snake Food
screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_pos = [(0,0), (-20,0) , (-40,0)]

# turtles = []
# for position in starting_pos:
#     new_Turtle = Turtle("square")
#     new_Turtle.color("white")
#     new_Turtle.penup()
#     new_Turtle.goto(position)
#     turtles.append(new_Turtle)
# screen.update()
# is_true = True
# #IDEA : there are 3 square turtles making up the snake [3][2][1] , so now if 1 turns left 2 and 3 dont follow they go in a straight line
# #hence if we move 3 to position of 2 then move 2 to position 1 and then move 1 by a single unit , [1] turning left will turn the snake completely
# while   is_true:
#     screen.update()
#     time.sleep(0.1)#Adds 0.1 sec delay after each turtle moves
#     # for turtle in turtles:
#     #    turtle.forward(20)
#     for turt_num in range(len(turtles) - 1 , 0 , -1): #range(start=  2, stop= 0 ,step= -1)
#         new_x = turtles[turt_num -1].xcor()#Second turtle
#         new_y = turtles[turt_num -1].ycor()#Second turtle
#         turtles[turt_num].goto(new_x,new_y)#Last Turtle
#     turtles[0].forward(20)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
