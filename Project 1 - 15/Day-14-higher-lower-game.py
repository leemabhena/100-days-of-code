# compare two things from data list for which is lower and which is higher randomly
# get guess from user
# B to become A
# play as long as you winning
from random import randint, choice
from Day_14_game_data import data
from Day_14_art import logo, vs
# create a function that return random generated A and B and print it to the screen
print(logo)

a = choice(data)
def random_data():
    """Return a random list with 2 items using a as a global variable"""
    global a
    b = choice(data)
    if a == b:
        b = choice(data)
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']} at {a['follower_count']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']} at {b['follower_count']}")
    rand_list = [a, b]
    a = b
    return rand_list

def compare(rand_list):
    a_fig = rand_list[0]['follower_count']
    b_fig = rand_list[1]['follower_count']
    user_guess = input('Who has more followers type "A" or "B" : ').upper()
    while user_guess not in ['A', "B"]:
        user_guess = input('Who has more followers type "A" or "B" : ').upper()
    guess = ''
    if user_guess == 'A':
        guess = 0
    elif user_guess == 'B':
        guess = 1
    # compare which is greater A or B
    if a_fig > b_fig and rand_list[guess]['follower_count'] == a_fig:
        return 'Win'
    elif b_fig > a_fig and rand_list[guess]['follower_count'] == b_fig:
        return "Win"
    else:
        return "Lose"


is_playing = True
count = 0
while is_playing:
    if count != 0:
        print(f'\nYou are right!!, current score is {count}.')
    results = compare(random_data())
    if results == "Lose":
        is_playing = False
        print(f"Sorry that was wrong, final score is {count}")
    count += 1

















