from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-295,y=260)
        self.points=0
        self.color("black")
        self.display()

    def Game_Over_Message(self):
        self.goto(x=-70,y=0)
        self.write(arg="GAME OVER",font=FONT)

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.points}", font=FONT)

