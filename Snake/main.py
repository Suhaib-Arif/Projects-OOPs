from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Last Serenade")

score = Score()
snake = Snake()
food = Food()

screen.tracer(0)

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

its_on=True
screen.update()
while its_on:
    screen.tracer(0)
    snake.move()
    screen.update()

    if snake.overlap():
        its_on=False
        score.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.gain_points()
        snake.increase_size()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        its_on=False
        score.game_over()
screen.exitonclick()
