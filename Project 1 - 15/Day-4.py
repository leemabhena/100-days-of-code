import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
choice = int(input("What do you choose. Type 0 for Rock, 1 for Paper and 2 for Scissors "))

print(choices[choice])

print('Computer chose: ')
computer_choice = random.randint(0, 2)
print(choices[computer_choice])

if choices[choice] == rock and choices[computer_choice] == scissors:
    print('You Win!!!!!!!!!!')
elif choices[choice] == scissors and choices[computer_choice] == rock:
    print('You Lose!!!!!!!!!!')
elif choices[choice] == choices[computer_choice]:
    print('Its a draw!!!!!!!!!!!')
if choices[choice] == scissors and choices[computer_choice] == paper:
    print('You Win!!!!!!!!!!')
elif choices[choice] == paper and choices[computer_choice] == scissors:
    print('You Lose!!!!!!!!!!')
if choices[choice] == paper and choices[computer_choice] == rock:
    print('You Win!!!!!!!!!!')
elif choices[choice] == rock and choices[computer_choice] == paper:
    print('You Lose!!!!!!!!!!')
else:
    print('You entered an invalid choice you lose.')