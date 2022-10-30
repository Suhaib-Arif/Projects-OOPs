from turtle import Turtle
FONT=("Arial",12,"normal")
class Score(Turtle):


    def __init__(self):
        self.score=0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=-60,y=280)
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Your score is now {self.score}",font=FONT)

    def game_over(self):
        self.goto(x=-100, y=0)
        self.write(arg=f"GAME OVER!!!! \n Final score is {self.score}", font=("Ariel", 24, "normal"))

    def gain_points(self):
        self.score+=1
        self.display()
