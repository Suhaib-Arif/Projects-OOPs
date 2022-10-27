from turtle import Turtle,Screen

screen = Screen()
screen.bgcolor("black")

color=["red", "green", "blue", "brown", "purple", "yellow"]

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make a bet",prompt="Which turtle do you think will win? pick a color")


# turtle = Turtle()
# turtle.color("white")
# turtle.setheading(225)
# turtle.forward(220)
# turtle.setheading(180)
# turtle.forward(60)
# print(turtle.position())

# (-215.56,-155.56)

y_cor=-155.56
my_turtles=[]
for i in range(6):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(color[i])
    turtle.goto(-215.56,y_cor)
    y_cor+=65
    my_turtles.append(turtle)

# print(my_turtles)

import random
Game_over = False
while not Game_over:
    for racer in my_turtles:
        step=random.randint(5,45)
        racer.forward(step)
        if racer.xcor() > 250:
            print(racer)
            Game_over=True
            winner = str(racer.pencolor())
            break


if user_bet == winner:
    print(f"Congratulations, {user_bet} turtle is the winner,you won")
else:
    print(f"It seems like {user_bet} turtle lost")
screen.exitonclick()
