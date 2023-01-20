from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPEED_CONTROL = 0.6


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=270, y=random.randint(-250, 250))
        self.color(random.choice(COLORS))
        self.setheading(180)

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1) * SPEED_CONTROL)
