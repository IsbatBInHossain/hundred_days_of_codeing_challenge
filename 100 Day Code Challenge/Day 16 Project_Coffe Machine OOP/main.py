from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    menu = Menu()
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == 'off':
        machine_on = False
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        order_name = menu.find_drink(order)
        cost = order_name.cost
        if coffee_maker.is_resource_sufficient(order_name) and money_machine.make_payment(cost):
            coffee_maker.make_coffee(order_name)
