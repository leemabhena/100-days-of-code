from Day_9_art import logo
print(logo)
another_bidder = True
bidders = {}
while another_bidder:
    name = input('What is your name: ')
    price = int(input('Whats your bid $'))
    bidders[name] = price
    another_user = input('Type "yes" if there is another bidder and "no" if there are no more bidders: ')
    if another_user == 'no':
        highest_bidder_price = 0
        for name, price in bidders.items():
            if price > highest_bidder_price:
                highest_bidder_price = price
                highest_bidder_name = name
        print(f"Highest bidder is {highest_bidder_name} at ${highest_bidder_price}")
        another_bidder = False