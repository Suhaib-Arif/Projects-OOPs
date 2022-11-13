from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.speed(1)
        self.color("white")
        self.shape("circle")
        self.xcord=0
        self.ycord=0
        self.change_y=10
        self.change_x=10

    def moove(self):
        self.xcord+=self.change_x
        self.ycord+=self.change_y
        self.goto(x=self.xcord, y=self.ycord)
    def restore(self):
        self.goto(0,0)
