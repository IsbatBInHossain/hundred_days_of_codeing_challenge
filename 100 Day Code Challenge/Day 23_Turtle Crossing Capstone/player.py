from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish(self, level, car_rate):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            if car_rate >= 1:
                car_rate = car_rate - 1
            return level+1, car_rate
        else:
            return level, car_rate

    def collision(self,car):
        if self.distance(car) <= 20:
            return 1
