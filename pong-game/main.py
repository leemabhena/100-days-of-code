from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Pong Game With Lee')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50 or ball.xcor() < -320 and l_paddle.distance(ball) < 50:
        ball.bounce_x()

    # detect if right player misses the ball
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
    # detect if left player misses the ball
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()





screen.exitonclick()

