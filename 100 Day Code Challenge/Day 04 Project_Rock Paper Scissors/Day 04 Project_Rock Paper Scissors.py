from random import randint

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

prompt = int(input("Type 1 for rock, 2 for paper or 3 for scissors. "))
com = randint(1,3)

if prompt == 1:
    print("You choose:\n")
    print(rock)
elif prompt == 2:
    print("You choose:\n")
    print(paper)
elif prompt == 3:
    print("You choose:\n")
    print(scissors)

if prompt>=1 and prompt<=3:
    if com == 1:
        print("\nComputer choose:\n")
        print(rock)
    elif com == 2:
        print("\nComputer choose:\n")
        print(paper)
    elif com == 3:
        print("\nComputer choose:\n")
        print(scissors)

if prompt == com:
    print("\nIt's a draw!")
elif (prompt == 1 and com == 3) or (prompt == 2 and com == 1) or (prompt == 3 and com == 2):
    print("\nYou win!")
else:
    print("\nYou lose!")