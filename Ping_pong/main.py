from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen=Screen()
screen.title("PONG GAME !!!!!!!!!!!!!!!!!!!!!!!!!")
screen.setup(height=600,width=800)
screen.tracer()
screen.bgcolor("black")

l_paddle= Paddle((350,0))
r_paddle= Paddle((-350,0))

screen.listen()

screen.onkey(fun=l_paddle.foreward, key="Up")
screen.onkey(fun=l_paddle.backewards, key="Down")

screen.onkey(fun=r_paddle.foreward, key="w")
screen.onkey(fun=r_paddle.backewards,key="s")

ball = Ball()
score=Score()
screen.update()
# speed=0.1
while True:
    ball.moove()
    # time.sleep(speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y*=-1
    if (ball.xcor() > 320 or ball.xcor() < -320) and (ball.distance(r_paddle) < 40 or ball.distance(l_paddle) < 40):
        # speed-=0.1
        ball.change_x*=-1

    if ball.xcor() > 400:
        score.l_score+=1
        del ball
        score.display()
        ball=Ball()

        ball.change_x *= -1

    if ball.xcor() < -400:
        score.r_score+=1
        score.display()
        del ball
        ball = Ball()

        ball.change_x*=-1

screen.exitonclick()
