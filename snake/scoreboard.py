from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_point = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score_point}",align="center",font=('Arial', 8, 'normal'))
        self.hideturtle()

    def refresh(self) :
        self.score_point += 1
        self.clear()
        self.write(f"Score: {self.score_point}",align="center",font=('Arial', 8, 'normal'))
