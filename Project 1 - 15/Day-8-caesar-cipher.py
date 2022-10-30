from Day_8_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text, shift):
#     cipher_text = ''
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         cipher_text += alphabet[new_position]
#     print(f"The encrypted word is {cipher_text}")
#
# def decrypt(text, shift):
#     cipher_text = ''
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         cipher_text += alphabet[new_position]
#     print(f"The decrypted message is {cipher_text}")
#
#
# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == 'decode':
#     decrypt(text, shift)

def caesar(text, shift, shift_direction):
    # if user type encode, encode the message
    end_text = ''
    if shift_direction == 'decode':
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {shift_direction}d word is {end_text}")



start_again = True
while start_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 25

    caesar(text, shift, direction)
    user_response = input('Would you like to start again, type "yes" to start and "no" to end \n')
    if user_response == 'no':
        print('goodbye!!!')
        start_again = False
    else:
        start_again = True
