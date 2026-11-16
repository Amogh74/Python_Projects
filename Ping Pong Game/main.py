from turtle import Screen
from Ball import Ball
from Paddle import Paddle
from ScoreBoard import Score
import time

screen = Screen()

screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.tracer(0)
#TODO Create and move a paddle of height = 100 , width =20 ,  x_pos = 350 , y_pos = 0

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350 , 0))
ball = Ball()
scoreboard = Score()
scoreboard.update()
screen.listen()
screen.onkey(paddle1.go_up,"w") #paddle 1 =  right paddle
screen.onkey(paddle1.go_dw,"s")

screen.onkey(paddle2.go_up,"Up")#paddle 2 = left paddle
screen.onkey(paddle2.go_dw,"Down")


game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    scoreboard.update()
    screen.update()
    ball.move()
    #Detect top/bottom ball collision
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    #Detect Collision with right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() >320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when R paddle misses
    if ball.xcor() >380:
        ball.reset_pos()
        scoreboard.L_point()

    #Detect when L paddle Misses:
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.R_point()
screen.exitonclick()
