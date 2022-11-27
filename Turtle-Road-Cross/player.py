from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.refreash()

    def upwards(self):
        self.forward(MOVE_DISTANCE)

    def win(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def refreash(self):
        self.hideturtle()
        self.goto(x=0, y=-280)
        self.setheading(90)
        self.showturtle()
