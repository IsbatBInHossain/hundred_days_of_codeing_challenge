from random import choice
from art import logo
from os import system
#from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = choice(cards)
  return card

def calculate_score(card_list):
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0
  elif sum(card_list)>21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
    return sum(card_list)
  else:
    return sum(card_list)

def compare(user_score, computer_score):
  if computer_score == 0:
    return "Opponent scored a blackjack. You Lose 😤"
  elif user_score == 0:
    return "You scored a blackjack. You win 😃"
  elif user_score > 21:
    return "You went over. You lose 😤"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😁"
  elif user_score == computer_score:
    return "Draw 🙃"
  else:
    return "You lose 😤"

def play_game():
  
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score {user_score}.")
    print(f"  Computer's first card: {computer_cards[0]}.")
    
    if user_score == 0 or computer_score == 0 or user_score>21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  
  while (sum(computer_cards) < 17):
    computer_cards.append(deal_card())
    
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand {user_cards}, final score {user_score}")
  print(f"Commmputer final hand {computer_cards}, final score {computer_score}")
  print(compare(user_score, computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  #clear()
  system('cls')
  play_game()