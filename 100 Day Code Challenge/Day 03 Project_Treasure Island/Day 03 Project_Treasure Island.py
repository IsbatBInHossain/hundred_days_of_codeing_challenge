print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You start you're journey at a small village. You've found a old treasure map that your granpa left behind.")
print("You've decided to follow the map and find the treasure.After several days of adventure you've come across a crossroad")
print("The map shows both roads leads you to the same place.")

prompt1 = input("Which road would you like to take? 'left' road or the 'right' road?  ").lower()

if prompt1 == 'left':
    print("\nAfter taking the left path you've came across a riverside village. The map shows thet you have to go to an island in the middle of the river.")
    print("After asking around you've learnt that a boat can take you to the island but you have to wait 7 hours for the boat to arrive.")
    print("You can see the island from the pier and the river seems calm. You can swim to the island in 20 minutes.")
    prompt2 = input("Do you want to 'wait' for the boat or 'swim' to the island?  ").lower()
    if prompt2 == 'wait':
        print("\nAfter waiting for 7 hours the boat has arrived. After thet you've rached the island safely.")
        print("Following the map you go to an old ruin. Here you see three doors in front of you.")
        prompt3 = input("Which door would you go through? 'red', 'yellow' or 'blue'?  ").lower()
        if prompt3 == 'yellow':
            print("\nAfter going through the door you've come to a room full of treasures.")
            print("Congratulations!!! You've found the treasure!")
        elif prompt3 == 'red':
            print("After going through the door you've fallen into a pit of fire and burned to death.\nGame Over")
        elif prompt3 == 'blue':
            print("After going through the door a hoard of starving beasts attack and kill you.\nGame Over.")
        else:
            print("Sorry, wrong choice.\nGame Over.")
    else:
        print("\nWhile crossing the river you've been attacked by a flock of giant trouts. The trouts have biten you to death.\nGame Over.")
else:
    print("\nAfter taking the path you've came across a dilapidated bridge. While crossing the bridge falls apart and you've fallen to your death.")
    print("Game Over")
