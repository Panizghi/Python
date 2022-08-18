from turtle import Screen, Turtle, color
import time
#setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tarcer(0) 

#body basics

start_pos = [(0,0),(-20,0),(-40,0)]

segments = []

for i in start_pos :
    new_seg = Turtle("square")
    new_seg.color("white")
    new_seg.penup  # no line trace on screen 
    new_seg.goto(i)
    segments.append(new_seg)



#move snakes 
end_game = False

while not end_game :
    screen.update()   # instead of moving as segments snake move as one block 
    time.sleep(1)
    
    for seg in range(len(segments)-1,0,step=1): # start from last segment until the first one with step of one

       #working in reverse order of segement so we can turn and move forward without an issue 
       # use the cooridante of the first seg to determine the cord the whole segment need to move to  
       new_x= segments[seg-1].xcor()  
       new_y= segments[seg-1].ycor()
       segments[seg].goto(new_x,new_y)
    segments[0].forward(10)
        
























screen.exitonclick()