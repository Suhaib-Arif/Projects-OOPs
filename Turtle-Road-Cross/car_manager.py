from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.step=MOVE_INCREMENT
        self.shape("square")
        self.penup()
        self.shapesize(1,2)
        self.setheading(180)
        colour=random.choice(COLORS)
        self.color(colour)
        ycoordinate=random.randint(-250,250)
        self.goto(x=300,y=ycoordinate)


    def drive(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def accelerate(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE+=self.step
