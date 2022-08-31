
from turtle import Screen
from snake import Snake
import time
#setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0) 

#body basics

snake =Snake()
screen.listen() #collect key events
#detect spcf keys
screen.onkey(snake.up , "Up") 
screen.onkey(snake.down , "Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left, "Left")

#move snakes 
end_game = False

while not end_game :
    screen.update()   # instead of moving as segments snake move as one block 
    time.sleep(0.1)
    snake.move()
    
   
        
























screen.exitonclick()