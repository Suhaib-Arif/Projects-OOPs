from turtle import Turtle,Screen

matt = Turtle()
screen = Screen()

def Forward():
    matt.forward(10)

def Backwards():
    matt.backward(10)

def Turn_left():
    matt.left(10)

def Turn_right():
    matt.right(10)

def Clear():
    screen.resetscreen()

screen.listen()

screen.onkey(fun=Forward, key="Up")
screen.onkey(fun=Backwards, key="Down")
screen.onkey(fun=Turn_right, key="Right")
screen.onkey(fun=Turn_left, key="Left")
screen.onkey(fun=Clear, key="c")

screen.exitonclick()
