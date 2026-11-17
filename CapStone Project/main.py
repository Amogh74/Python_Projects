import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(player.Move,"Up")
game_is_on = True
car_manager = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_c()
    #detect collision
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            score.game_over()
            game_is_on = False

        #Detect successfull crossing
        if player.finished_race():
            player.goto_strt()
            car_manager.level_up()
            score.increase_lvl()

screen.exitonclick()
