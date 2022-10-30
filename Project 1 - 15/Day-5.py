#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_choosen = ''
for i in range(0 , nr_letters):
    random_number = random.randint(0, len(letters) -1 )
    letters_choosen += letters[random_number]
# print(letters_choosen)

numbers_choosen = ''
for i in range(0 , nr_numbers):
    random_number = random.randint(0, len(numbers) -1 )
    numbers_choosen += numbers[random_number]
# print(numbers_choosen)

symbols_choosen = ''
for i in range(0 , nr_symbols):
    random_number = random.randint(0, len(symbols) -1 )
    symbols_choosen += symbols[random_number]
# print(symbols_choosen)

password = letters_choosen + symbols_choosen + numbers_choosen
password_list = []
for i in range(0, len(password)):
    password_list.append(password[i])
# print(password_list)

random.shuffle(password_list)
# print(password_list)
shuffled_pass = ''.join(password_list)

print(f"Your password is: {shuffled_pass}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P