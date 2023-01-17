# from replit import clear

from art import logo
print(logo)

auction_list = {}
cont = True

while(cont):
  name = input("What is your name?: ")
  price = int(input("What's your bid?: $"))
  auction_list[name] = price
  bidder = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if bidder == 'yes':
    cont = True
  elif bidder == 'no':
    cont = False
#   clear()

count = 0
for bidder_name in auction_list:
  if auction_list[bidder_name] > count:
    highest_bidder = bidder_name
    count = auction_list[bidder_name]

print(f"The highest bidder is {highest_bidder} with a bid of ${count}.")
    