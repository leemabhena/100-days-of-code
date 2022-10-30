from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title('Turtle Race')
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color")
if user_bet:
    is_game_on = True
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y = 125
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.setposition(x=-230, y=y)
    new_turtle.color(colors[turtle_index])
    y = y - 50
    all_turtles.append(new_turtle)

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You won, {winning_color} was the winning turtle")
            else:
                print(f"You lost, {winning_color} was the winning turtle")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
