from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
from random import choice, randint
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = randint(1, 6)
        if random_num == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(280, randint(-250, 250))
            new_car.setheading(180)
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
