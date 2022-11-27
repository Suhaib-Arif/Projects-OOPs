import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score=Scoreboard()

player = Player()
car_list=[]

screen.listen()
turn=0
game_is_on = True

while game_is_on:
    if turn % 6 == 0:
        car_list.append(CarManager())
    time.sleep(0.1)
    screen.update()

    screen.onkey(fun=player.upwards, key="Up")

    for car in car_list:
        car.drive()
        if car.distance(player) <= 20:
            game_is_on=False
            score.Game_Over_Message()

    if player.win():
        score.points+=1
        player.refreash()
        car.accelerate()

    score.display()
    turn += 1


screen.exitonclick()
