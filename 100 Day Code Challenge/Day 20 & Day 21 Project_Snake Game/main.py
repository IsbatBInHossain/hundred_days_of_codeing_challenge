from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from score_board import ScoreBoard

screen = Screen()
snake = Snake()
food = Food()
score_board = ScoreBoard()
SPEED = 0.1
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True

while game_on:
    time.sleep(SPEED)
    screen.update()
    snake.move()
    headless_snake = snake.segments[1:]
    for segment in headless_snake:
        if snake.head.distance(segment) < 10 or not snake.wall_collision():
            game_on = False
            score_board.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score_increment()

screen.exitonclick()
