# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("chartreuse4")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",['Pikachu', 'Squirtle', 'Charmander', 'MewTwo'])
table.align = "l"
table.add_column("Type",['Electric', 'Water', 'Fire'])
print(table)
