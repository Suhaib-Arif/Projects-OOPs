from turtle import Turtle

PONG_WIDTH = 1
PONG_HEIGHT = 4

class Paddle(Turtle):
    def __init__(self,tuple):
        super(Paddle, self).__init__()
        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.shapesize(PONG_WIDTH, PONG_HEIGHT)
        self.penup()
        self.goto(tuple)
        self.setheading(90)
        self.showturtle()
    def foreward(self):
        self.forward(20)

    def backewards(self):
        self.backward(20)
