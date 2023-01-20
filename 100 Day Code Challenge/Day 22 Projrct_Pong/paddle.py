from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(position)

    def up(self):
        if self.ycor() <= 250:
            new_y = self.ycor()+20
            self.goto(x=self.xcor(), y=new_y)

    def down(self):
        if self.ycor() >= -230:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)


class Opponent(Paddle):
    def __init__(self, position):
        super().__init__(position)
        self.speed(6)
        self.y_coordinates = []  # list to store the ball's y-coordinates
        self.average_y = 0
        self.num_coordinates = 10  # number of coordinates to average

    def follow_ball(self, ball):
        self.y_coordinates.append(ball.ycor())
        if len(self.y_coordinates) > self.num_coordinates:
            self.y_coordinates.pop(0)
        self.average_y = sum(self.y_coordinates) / len(self.y_coordinates)
        if self.average_y > self.ycor():
            self.up()
        elif self.average_y < self.ycor():
            self.down()
