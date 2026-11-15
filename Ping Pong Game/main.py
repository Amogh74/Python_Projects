#Implimentation of Ping Pong Game
from turtle import Screen
from Paddle import Paddle
screen = Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.tracer(0)
#TODO Create and move a paddle of height = 100 , width =20 ,  x_pos = 350 , y_pos = 0

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350 , 0))


screen.listen()
screen.onkey(paddle1.go_up,"w") #paddle 1 =  right paddle
screen.onkey(paddle1.go_dw,"s")

screen.onkey(paddle2.go_up,"Up")#paddle 2 = left paddle
screen.onkey(paddle2.go_dw,"Down")

game_is_on =True
while game_is_on:
    screen.update()
screen.exitonclick()
