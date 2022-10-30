import turtle as t
from random import choice
# import colorgram
#
# colors = colorgram.extract('spot_painting.jpg', 30)
# rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
color_list = [(204, 157, 110), (105, 109, 128), (139, 142, 159), (222, 211, 120), (218, 233, 221), (165, 79, 48), (193, 144, 168), (107, 113, 169), (174, 156, 47), (17, 23, 60), (229, 167, 195), (216, 81, 60), (16, 37, 19), (145, 83, 96), (145, 161, 149), (37, 34, 15), (95, 112, 98), (197, 81, 99), (235, 172, 160), (181, 22, 9), (45, 48, 111), (176, 20, 35), (42, 21, 40), (181, 179, 220), (179, 202, 181), (115, 137, 120), (220, 208, 20)]

my_turtle = t.Turtle()
t.colormode(255)
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setposition(-200, -200)
y = -150
for i in range(10):
    for n in range(10):
        my_turtle.dot(15, choice(color_list))
        my_turtle.forward(50)
    my_turtle.goto(-200, y)
    y += 50

screen = t.Screen()
screen.exitonclick()