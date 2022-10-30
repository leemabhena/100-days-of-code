from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()
screen.listen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clear_srn():
    tim.setposition(0, 0)
    tim.setheading(0)
    tim.clear()

def clockwise():
    location = tim.heading()
    tim.setheading(location + 10)

def anti_clockwise():
    location = tim.heading()
    tim.setheading(location - 10)


screen.onkey(fun=move_forward, key='Right')
screen.onkey(fun=clear_srn, key='c')
screen.onkey(fun=move_backward, key="Left")
screen.onkey(fun=clockwise, key='Up')
screen.onkey(fun=anti_clockwise, key='Down')
screen.exitonclick()
