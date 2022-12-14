from turtle import Turtle

START_POS = [(0,0),(-20,0),(-40,0)]  
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments =[]
        self.create()
        

    def create(self):
        for pos in START_POS :
            self.add_seg(pos)
    
    def add_seg(self,pos) :
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()  # no line trace on screen 
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1): # start from last segment until the first one with step of one

            #working in reverse order of segement so we can turn and move forward without an issue 
            # use the cooridante of the first seg to determine the cord the whole segment need to move to  
            new_x= self.segments[seg-1].xcor()  
            new_y= self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def refresh(self):
        self.add_seg(self.segments[-1].position())
    #use -1 to apped to last segment 
    #position() is turtle method 


    # when the head move up the rest of the segments will follow along due to continuous upadate of move method

    def up(self) : 
        if self.segments[0].heading() != 270 : #snake dont move back onn its self 
            self.segments[0].setheading(90) 
    
    def down(self) :
        if self.segments[0].heading() != 90 :
            self.segments[0].setheading(270)

    def left(self) :
        if self.segments[0].heading() != 0 :
            self.segments[0].setheading(180)
    
    def right(self) :
        if self.segments[0].heading() != 180 :
            self.segments[0].setheading(0)

