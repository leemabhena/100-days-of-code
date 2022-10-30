from turtle import Turtle, Screen
import random

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple([r, g, b])

# my_turtle = Turtle()
# sides = [3, 4, 5, 6, 7, 8, 9, 10]
# colors = [ 'red', 'blue', 'brown', 'green', 'coral', 'cyan', 'DeepPink', "chocolate"]
#
# for side in range(len(sides)):
#     angle = 360 / sides[side]
#     for i in range(sides[side]):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#     my_turtle.color(colors[side])
#
#
# screen = Screen()
# screen.exitonclick()


# tim = Turtle()
# my_funcs = [tim.forward, tim.backward, tim.right, tim.left]
#
# tim.pensize(5)
# tim.speed('fastest')
# angle = 90
# pace = 30
# colors = ['red', 'blue', 'brown', 'green', 'coral', 'cyan', 'DeepPink', "chocolate"]
# i = 0
# screen = Screen()
# screen.colormode(255)
# while i < 1000:
#     num = random.randint(0, 3)
#     if num == 0 or num == 1:
#         my_funcs[num](pace)
#     else:
#         my_funcs[num](angle)
#
#     tim.pencolor(random_colour())
#     i += 1
#
#
# screen.exitonclick()


tom = Turtle()
screen = Screen()
screen.colormode(255)

tom.speed('fastest')
def draw_spirograph(shift_size):
    for i in range(360 // shift_size):
        tom.color(random_colour())
        tom.circle(100)
        tom.setheading(tom.heading() + shift_size)


draw_spirograph(5)


screen.exitonclick()