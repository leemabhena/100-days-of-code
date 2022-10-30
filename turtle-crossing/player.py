from turtle import Turtle
import car_manager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLLISION_DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def move_forward(self):
        x_cor, y_cor = self.xcor(), self.ycor() + MOVE_DISTANCE
        if self.ycor() <= FINISH_LINE_Y:
            self.goto(x_cor, y_cor)

    def has_collided(self, car):
        car_cor = car.position()
        if self.distance(car_cor) <= COLLISION_DISTANCE:
            return True
        return False

    def end_of_screen(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
