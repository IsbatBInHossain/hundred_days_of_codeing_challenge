from turtle import Screen, Turtle
from paddle import Paddle  # Opponent
from ball import Ball
from score_board import Score
import time

SLEEP = 0.01
STARTING_POSITION = (475, 0)
ENEMMY_POSITION = (-480, 0)

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=1000, height=600)
court_maker = Turtle()
court_maker.pencolor("white")
my_score = Score((50, 230))
enemy_score = Score((-50, 230))


def draw_court():
    court_maker.penup()
    court_maker.hideturtle()
    court_maker.goto(0, -300)
    court_maker.setheading(90)
    while court_maker.ycor() <= 300:
        court_maker.pendown()
        court_maker.forward(10)
        court_maker.penup()
        court_maker.forward(10)


def point_counter():
    if ball.xcor() >= 500:
        ball.refresh(2)
        enemy_score.increase_score()

    elif ball.xcor() <= -500:
        ball.refresh(1)
        my_score.increase_score()

    if my_score.score < 10 and enemy_score.score < 10:
        return True
    else:
        return False


def game_over(game_over_turtle):
    game_over_turtle.hideturtle()
    game_over_turtle.color("white")
    game_over_turtle.write(arg="Game Over", align="center", font=("Courier", 40, "bold"))


declare_turtle = Turtle()
draw_court()
ball = Ball()
my_paddle = Paddle(STARTING_POSITION)
screen.update()
enemy_paddle = Paddle(ENEMMY_POSITION)


# opponent = Opponent(ENEMMY_POSITION)


screen.update()
screen.listen()
screen.onkeypress(fun=my_paddle.up, key="Up")
screen.onkeypress(fun=my_paddle.down, key="Down")
screen.onkeypress(fun=enemy_paddle.up, key="w")
screen.onkeypress(fun=enemy_paddle.down, key="s")
game_on = True
score = 0

while game_on:
    time.sleep(SLEEP)
    ball.move()
    ball.wall_collision()
    ball.collide(my_paddle)
    ball.collide(enemy_paddle)
    game_on = point_counter()
    # opponent.follow_ball(ball)
    screen.update()

ball.clear()
game_over(declare_turtle)
screen.update()
screen.exitonclick()
