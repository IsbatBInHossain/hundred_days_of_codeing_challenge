from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = -1
        self.penup()
        self.goto(position)
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=self.score, align=ALIGNMENT, font=FONT)
