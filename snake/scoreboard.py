from turtle import Turtle
FONT = ('Arial', 8, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_point = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score_point}",align="center",font=FONT)
        self.hideturtle()

    def refresh(self) :
        self.score_point += 1
        self.clear()
        self.write(f"Score: {self.score_point}",align="center",font=('Arial', 12, 'normal'))
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"High Score: {self.score_point}\nGAME OVER!",align="center",font=('Arial', 12, 'normal'))