MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# prompt the user of what they would like to order
# check resources sufficient, Print sorry there is not enough...
# ask for coins and process
# check if money is enough, refund if not and start again
# if enough calculate change and serve the coffee
# print report Water:100ml, Milk: ml, Money : $
# type off to switch off or end program
def check_resources(beverage):
    water = MENU[beverage]['ingredients']['water']
    coffee = MENU[beverage]['ingredients']['coffee']
    is_enough = 1
    if water > resources['water']:
        print('Sorry there is not enough water')
        is_enough = 0
    if coffee > resources['coffee']:
        print('Sorry there is not enough coffee')
        is_enough = 0
    if order != 'espresso':
        milk = MENU[beverage]['ingredients']['milk']
        if milk > resources['milk']:
            print('Sorry there is not enough milk')
            is_enough = 0
    return is_enough

def process_coin(beverage, total):
    cost = MENU[beverage]['cost']
    is_enough = 1
    if total < cost:
        print('Your money is not enough, Here is your refund')
        is_enough = 0
    else:
        change = total - cost
        print(f'Here is your change ${change:0.2f}')
    return is_enough


another_order = True
money = 0
while another_order:
    order = input('What would you like? (espresso / latte / cappuccino): ')
    if order == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        continue
    elif order == 'off':
        break
    else:
        resources_enough = check_resources(order)
    if resources_enough == 0:
        continue
    print('Please insert some coins')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))

    total_cost = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    coins = process_coin(order, total_cost)
    if coins == 0:
        continue
    else:
        # code to reduce my resources
        resources["water"] -= MENU[order]['ingredients']['water']
        resources["coffee"] -= MENU[order]['ingredients']['coffee']
        if order != 'espresso':
            resources["milk"] -= MENU[order]['ingredients']['milk']
        money += MENU[order]['cost']

    print(f"Here is your {order}. Enjoy")














