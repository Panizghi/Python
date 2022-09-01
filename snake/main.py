
from turtle import Screen
from food import Food
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
food = Food()
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
    time.sleep(0.09) 
    snake.move()
    #use distance method to find collsion of the food with snake
    if snake.segments[0].distance(food) < 15: # food is 10 by 10 considering buffer 15 px should be reasonable
       food.refresh()
   
        
























screen.exitonclick()