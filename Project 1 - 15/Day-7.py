import random
from Day_7_hangman_words import word_list
from Day_7_hangman_art import logo, stages

print(logo)
# choose a random word
chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}")
# ask user to guess a letter
display = ["_" for i in range(0, len(chosen_word))]
# guess = input('Guess a letter: ').lower()

# check if the letter guessed is in chosen word
# for i in range(0, len(chosen_word)):
#     if chosen_word[i] == guess:
#         display[i] = guess
# print(display)

lives = 6
current_run = 0
end_of_game = False
while not end_of_game:

    guess = input('Guess a letter: ').lower()
    if guess in display:
        print(f'You guessed {guess}. Note you have already guessed it.')
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(f"{' '.join(display)}")
    if '_' not in display:
        print("You win!!")
        end_of_game = True
    if guess not in chosen_word:
        print(stages[lives])
        print(f'You guessed {guess} and it is not in word, You will lose a life...')
        lives = lives - 1

    if lives < 0:
        print('You Lose!!')
        end_of_game = True

