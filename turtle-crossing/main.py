import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(play.move_forward, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # Detect Collision
    for car in car_manager.all_cars:
        if play.has_collided(car):
            score_board.game_over()
            game_is_on = False
    # Detect if player has reached end of screen
    if play.end_of_screen():
        play.go_to_start()
        car_manager.level_up()
        score_board.update()

screen.exitonclick()

