import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
cities = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / {len(data)} States correct", prompt="Whats another state's name ?").title()
    if answer_state == 'Exit':
        break
    if answer_state in cities:
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        state_data = data[data.state == answer_state]
        text.goto(int(state_data.x), int(state_data.y))
        text.write(answer_state)
        guessed_states.append(answer_state)

to_learn = [state for state in cities if state not in guessed_states]
new_data = pandas.DataFrame(
    {
        'state': to_learn,
    }
)
new_data.to_csv('state_to_learn.csv')