from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_text(self, position, argument):
        self.clear()
        self.goto(position)
        self.write(arg=argument, align="center", font=FONT)
