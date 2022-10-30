import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)
    return {'user_sum': user_sum, 'computer_sum': computer_sum, 'user_cards': user_cards, 'computer_cards': computer_cards}


results = deal_card()
print(f"Your cards {results['user_cards']}, current score {results['user_sum']}" )
print(f"Computer's first card is {results['computer_cards'][0]}")

def black_jack():
    still_playing = True
    while still_playing:

        if results['user_sum'] == 21:
            print('You win')
            still_playing = False
        elif results['computer_sum'] == 21:
            print('computer wins')
            still_playing = False
        if results['user_sum'] > 21:
            if 11 in results['user_cards']:
                user_card = results['user_cards']
                position = user_card.index(11)
                user_card[position] = 1
                new_user_sum = sum(user_card)
                if new_user_sum > 21:
                    print('You Lose')
                    still_playing = False
                else:
                    another_card = input("Type 'y' to get another card and 'n' to exit")
                    if another_card == 'y':
                        list1 = results['user_cards']
                        list1.append(random.choice(cards))
                        black_jack()
            else:
                print('You lose')
                still_playing = False
        else:
            another_card = input("Type 'y' to get another card and 'n' to exit")
            if another_card == 'y':
                list1 = results['user_cards']
                list1.append(random.choice(cards))
                black_jack()


black_jack()
# check for winner
new_users_sum = sum(results['user_cards'])
new_comp_results = results['computer_cards']
new_comp_results.append(random.choice(cards))
new_comp_sum = sum(new_comp_results)

if new_comp_sum > 21:
    print('You win')
elif new_comp_sum > new_users_sum:
    print('Computer wins')
elif new_users_sum > new_comp_sum:
    print('User wins')
else:
    print('Its a draw')
