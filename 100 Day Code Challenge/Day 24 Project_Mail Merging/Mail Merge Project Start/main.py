with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt') as f1:
    letter = f1.readlines()

with open('../Mail Merge Project Start/Input/Names/invited_names.txt') as f1:
    names = f1.readlines()

name_list = []
for name in names:
    name_list.append(name.replace("\n", ''))

for name in name_list:
    letter[0] = f"Dear {name},\n"
    with open(f'Output/ReadyToSend/letter_for_{name}.txt', mode='w') as file:
        file.writelines(letter)
