from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = -1
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score_increment()

    def score_increment(self):
        self.score += 1
        self.clear()
        scr = f"Score: {self.score}"
        self.write(scr, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)
