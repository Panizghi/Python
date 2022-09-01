from random import randint
from turtle import Turtle 
class Food(Turtle) :

    def __init__(self) :
        super().__init__() #inheritance
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        # random food color bit nice than nokia version :)
        self.color("yellow")
        self.speed("fastest")
        

    def refresh(self) :
        self.goto(randint(-280,280),randint(-280,280))