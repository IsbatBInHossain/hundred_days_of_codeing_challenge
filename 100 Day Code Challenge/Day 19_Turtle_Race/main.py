import turtle
from turtle import Turtle, Screen
from random import randint


def turtle_init(turtle_name, color, y):
    turtle_name.penup()
    turtle_name.shape("turtle")
    turtle_name.speed("slowest")
    turtle_name.color(color)
    turtle_name.goto(-230, y)


def race(distance):
    tmnt = [leonardo, michaelangelo, raphael, donatello]
    while tmnt[0].xcor() < distance and tmnt[1].xcor() < distance and tmnt[2].xcor() < distance and \
            tmnt[3].xcor() < distance:
        for ninja_turtle in tmnt:
            if ninja_turtle.xcor() < distance:
                ninja_turtle.forward(randint(0, 10))


def winner_determiner():
    leo_distance = leonardo.xcor()
    mike_distance = michaelangelo.xcor()
    raph_distance = raphael.xcor()
    don_distance = donatello.xcor()
    distance = {
        "blue": leo_distance,
        "orange": mike_distance,
        "red": raph_distance,
        "purple": don_distance,
    }
    return max(distance, key=distance.get)


screen = Screen()
screen.setup(width=500, height=400)
leonardo = Turtle()
michaelangelo = Turtle()
raphael = Turtle()
donatello = Turtle()
bet = turtle.textinput("Bet", "Place your bet").lower()

turtle_init(leonardo, "blue", 120)
turtle_init(michaelangelo, "orange", 60)
turtle_init(raphael, "red", 0)
turtle_init(donatello, "purple", -60)

race(230)
winner = winner_determiner()
if bet == winner:
    print(f"Congratulations, you win! The {winner} turtle was the winner.")
else:
    print(f"You lose! The {winner} turtle was the winner.")

screen.bye()
