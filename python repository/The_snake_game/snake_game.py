from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600 ,height=600)
screen.bgcolor("Black")
screen.tracer(0)

screen.title("Snake Game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
    
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()  

    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            pass
        elif snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
    snake.move()

screen.exitonclick()