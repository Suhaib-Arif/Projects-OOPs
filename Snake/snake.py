import time
from turtle import Turtle


MOVE_FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        x_cor=0
        self.segment=[]
        for _ in range(3):
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(x_cor, 0)

            x_cor -= 20
            self.segment.append(turtle)
        self.head=self.segment[0]
        self.speed = 0.05
    def move(self):
        for seg_index in range(len(self.segment) - 1, 0, -1):
            next_tur_pos = self.segment[seg_index - 1].pos()
            self.segment[seg_index].goto(next_tur_pos)
            time.sleep(self.speed)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def increase_size(self):
        part=Turtle("square")
        part.color("white")
        part.penup()

        self.segment.append(part)
    def overlap(self):
         for seg in self.segment[1:]:
             if self.head.distance(seg) < 10:
                return True
    # def disable(self):
