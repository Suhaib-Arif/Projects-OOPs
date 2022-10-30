from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):

        random_x= randint(-280,280)
        random_y= randint(-280,280)
        self.goto(random_x,random_y)
        self.showturtle()
