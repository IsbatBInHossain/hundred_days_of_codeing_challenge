import turtle
from turtle import Turtle
import random

BALL_SHAPE = "circle"
SPEED = 5
turtle.mode("standard")
turtle.degrees()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.penup()
        self.speed("fastest")
        self.ball_speed = SPEED
        self.turtlesize(0.8, 0.8)
        self.color("white")
        self.setheading(random.randint(-25, 25))

    def move(self):
        self.forward(self.ball_speed)

    def wall_collision(self):
        if not (-290 <= self.ycor() <= 290):
            self.setheading(360 - self.heading())

    def collide(self, paddle):
        if (paddle.ycor() + 50 > self.ycor() > paddle.ycor() - 50) and (
                paddle.xcor() - 20 < self.xcor() < paddle.xcor() + 20):
            heading = self.heading() + random.randint(-10, 10)
            self.setheading(180 - heading)
            self.ball_speed += 0.5

    def refresh(self, x):
        self.home()
        if x == 1:
            self.setheading(random.randint(-25, 25))
            self.ball_speed = SPEED

        if x == 2:
            self.setheading(random.randint(155, 205))
            self.ball_speed = SPEED
