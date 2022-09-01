
from turtle import Screen
from food import Food
from scoreboard import Score
from snake import Snake
import time
#setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0) 

#body basics
snake = Snake()
food = Food()
score = Score()
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
       score.refresh()
       snake.refresh()
       food.refresh()
   
    if snake.segments[0].xcor() <-280 or snake.segments[0].xcor() >280 or snake.segments[0].ycor() <-280 or snake.segments[0].ycor() >280 :
        end_game = True
        score.gameover()

    for segment in snake.segments[1:] : #passing head by slicing 
    
        if snake.segments[0].distance(segment) < 10 :
            end_game = True
            score.gameover()























screen.exitonclick()