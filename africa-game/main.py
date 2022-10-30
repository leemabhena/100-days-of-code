import turtle
import pandas

screen = turtle.Screen()
screen.title("Maps of Africa")
image = "map_of_africa.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click(x, y):
#     country = screen.textinput(title="Enter a country of your choice", prompt="Another Country")
#     text = f"{country},{x},{y}\n"
#     with open("countries.txt", mode="a") as country_file:
#         country_file.write(text)
# turtle.onscreenclick(get_mouse_click)
data = pandas.read_csv("countries.csv")

countries = data['country'].to_list()
guessed_list = []

while True:
    answer = screen.textinput(title=f"{len(guessed_list)} / {len(data)} Countries Correct",
                              prompt="Enter another country's name").title()
    if answer in countries:
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        selected_country = data[data.country == answer]
        print(selected_country)
        text.goto(int(selected_country.x), int(selected_country.y))
        text.write(f'*{answer}')
        guessed_list.append(answer)

screen.mainloop()
