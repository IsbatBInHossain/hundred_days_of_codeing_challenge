import turtle
from random import choice
from turtle import Turtle, Screen
# from color_extractor import color_list

turtle.colormode(255)
screen = Screen()
timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.setposition(-250, -200)


def turtle_turn(forward):
    if timmy.heading() == 0:
        timmy.lt(90)
        timmy.forward(forward)
        timmy.lt(90)
    else:
        timmy.rt(90)
        timmy.forward(forward)
        timmy.rt(90)
    timmy.forward(forward)


def dot_maker(forward, dot):
    for _ in range(round(10)):
        for _ in range(round(10)):
            color = choice(color_pallet)
            timmy.pendown()
            timmy.dot(dot, color)
            timmy.penup()
            timmy.forward(forward)
        turtle_turn(forward)


forward_step = 50
dot_size = 20
color_pallet = [(235, 240, 244), (2, 13, 31), (53, 25, 17), (219, 127, 106), (9, 105, 159), (242, 213, 68),
                (149, 83, 39), (215, 87, 64), (164, 162, 32), (158, 7, 24), (157, 62, 102), (11, 62, 31),
                (206, 74, 104), (97, 6, 20), (11, 96, 57), (173, 135, 162), (0, 63, 145), (7, 172, 216), (157, 33, 23),
                (4, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (101, 219, 229), (221, 178, 217),
                (80, 135, 179)]
dot_maker(forward_step, dot_size)
screen.exitonclick()
