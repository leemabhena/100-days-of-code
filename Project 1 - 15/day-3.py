

print("Welcome to treasure island, your goal is to find a map....")

direction = input("You come across a railroad which way would you choose left or right").lower()

if direction == 'left':
    print("You come across a lack, do you swim or wait")
    swim_wait = input("Swim or wait").lower()
    if swim_wait == 'wait':
        print("You come across three doors, red, blue and yellow which one do you choose")
        door = input("Yellow, Green or Blue").lower()
        if door == 'yellow':
            print('You win')
        else:
            print("You lose")
    else:
        print("Game over you lose")
else:
    print("Game over you lose")
