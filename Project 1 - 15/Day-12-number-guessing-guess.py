import random
print('Welcome to the number guessing game')
print('Im thinking of a number between 1 and 100')

# choose a random number between 1 and 100

random_num = random.randint(1, 101)
def check_difficulty():
    # check for level of difficulty if easy award 10 lives and hard 5 lives
    difficult = input('Choose a difficulty. Type "easy" or "hard": ')
    # keep track of number of plays left
    if difficult == 'easy':
        return 10
    else:
        return 5

# choose a number until number of plays is zero
# check if player has won

def guess_number(number_of_plays, random_number):
    win = 0
    while number_of_plays > 0:
        print(f'You have {number_of_plays} attempts remaining to play the game.')
        user_guess = int(input('Make a guess : '))
        # check if user's guess is correct
        if user_guess > random_number:
            print('Too high')
        elif user_guess < random_number:
            print('Too low')
        else:
            print('Correct')
            win = 1
            break

        # decrease number of plays
        number_of_plays -= 1
        # check if win
        if number_of_plays == 0 and win == 0:
            print('You Lose')


play_again = True
while play_again:
    guess_number(check_difficulty(), random_num)
    play = input("Type 'y' to play again and 'n' to quit ")
    if play == 'n':
        print("Thanks for playing")
        play_again = False


