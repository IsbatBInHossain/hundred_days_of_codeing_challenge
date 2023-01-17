from art import logo
from random import randint

print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")

difficulity = input ("Choose a difficulty. Type 'easy' or 'hard': ").lower()
chosen_number = randint(1,100)
if difficulity == 'easy':
  number_of_life = 10
else:
  number_of_life = 5

is_game_over = False

while number_of_life > 0 and not is_game_over:
  print(f"You have {number_of_life} attempts remaining to guess the number.")
  player_guess = int(input("Make a guess: "))
  if player_guess == chosen_number:
    is_game_over = True
    print(f"You got it! The answer was {chosen_number}.")
  elif player_guess > chosen_number:
    print("Too high\nGuess again.")
    number_of_life -=1
  else:
    print("Too low\nGuess again.")
    number_of_life -=1

if number_of_life == 0:
  print("You've run out of guesses, you lose.")
  