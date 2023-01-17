import random
from os import system
import art
from game_data import data


def fetch_data(sl_no):
    """Take a serial no. as input and returns the description of the data entry"""

    entity = data[sl_no]
    return f"{entity['name']}, a {entity['description']}, from {entity['country']}"


def higher_lower(sl_no_1, sl_no_2):
    """Takes two serial no. as inputs and returns the serial no. with higher follower"""

    follower1 = data[sl_no_1]['follower_count']
    follower2 = data[sl_no_2]['follower_count']
    if follower1 > follower2:
        return 'a'
    else:
        return 'b'


def game():
    is_game_over = False
    point = 0
    pos_1 = random.randint(0, 49)
    pos_2 = random.randint(0, 49)
    while pos_1 == pos_2:
        pos_2 = random.randint(0, 49)

    while not is_game_over:
        print(art.logo)
        if point != 0:
            print(f"You're right! Current score: {point}.")
        print(f"Compare A: {fetch_data(pos_1)}\n")
        print(art.vs)
        print(f"Against B: {fetch_data(pos_2)}\n")
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        ans = higher_lower(pos_1, pos_2)
        if user_input == ans:
            point += 1
            pos_1 = pos_2
            while pos_1 == pos_2:
                pos_2 = random.randint(0, 49)
                system('cls')
        else:
            is_game_over = True
            system('cls')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {point}")


game()
