import turtle
from random import randint
from turtle import Turtle, Screen

turtle.colormode(255)
screen = Screen()
timmy = Turtle()
timmy.speed("fastest")


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def spirograph(size_of_gap):
    angle = 0
    while angle <= 360:
        timmy.setheading(angle)
        timmy.color(random_color())
        timmy.circle(100)
        angle += size_of_gap


spirograph(4)
# spirograph(int(input("What size of gap do you want? ")))
screen.exitonclick()
