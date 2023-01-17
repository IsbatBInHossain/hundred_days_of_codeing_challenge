import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")


def turn_right():
    tim.setheading(tim.heading() - 10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def move_up():
    tim.forward(10)


def move_down():
    tim.backward(10)


def clear():
    turtle.resetscreen()


screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")
screen.listen()




screen.exitonclick()