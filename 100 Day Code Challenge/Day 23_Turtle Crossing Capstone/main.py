import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_RATE = 6

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtlr Crossing")
screen.listen()
player = Player()
screen.onkeypress(fun=player.move, key="Up")

score_board = Scoreboard()
score_board2 = Scoreboard()


def car_generator(car_generation_rate):
    if random.randint(1, car_generation_rate) == 1:
        new_car = CarManager()
        return new_car


garage = []
game_is_on = True
level = 1
car_rate = 6
while game_is_on:
    time.sleep(0.1)
    level, car_rate = player.finish(level, car_rate)
    cars = car_generator(car_rate)
    arg = f"Level: {level}"
    score_board.write_text(position=(-200, 250), argument=arg)
    if cars is not None:
        garage.append(cars)
    for car in garage:
        if car.xcor() >= -310:
            car.move(level)
            if player.collision(car) == 1:
                game_is_on = False
        else:
            garage.remove(car)
            car.clear()
            car.hideturtle()
    screen.update()

score_board2.write_text(argument="Game Over", position=(0, 0))
screen.exitonclick()
