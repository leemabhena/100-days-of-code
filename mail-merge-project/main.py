
with open("./Input/Letters/starting_letter.txt") as template:
    letter = template.read()

with open('./Input/Names/invited_names.txt') as invited:
    names = invited.readlines()

for name in names:
    personalised_letter = letter.replace("[name]", name.strip())
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as send:
        send.write(f"{personalised_letter}")

