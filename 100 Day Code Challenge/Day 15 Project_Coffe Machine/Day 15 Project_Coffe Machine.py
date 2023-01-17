MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCE = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }


def report(money,resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def resource_manager(coffee_name,resources):
    if MENU[coffee_name]["ingredients"]["water"] > resources["water"]:
        return "Sorry, Not enough water"
    elif MENU[coffee_name]["ingredients"]["milk"] > resources["milk"]:
        return "Sorry, Not enough milk"
    elif MENU[coffee_name]["ingredients"]["coffee"] > resources["coffee"]:
        return "Sorry, Not enough coffee"
    else:
        return 0


def coin_processing(coffee):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    total_money = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    if total_money >= MENU[coffee]["cost"]:
        change = round(total_money - MENU[coffee]["cost"],2)
        print(f"Here is ${change:.2f} in change.")
        return MENU[coffee]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def resource_deductor(coffee,resource):
    water = resource["water"] - MENU[coffee]["ingredients"]["water"]
    milk = resource["milk"] - MENU[coffee]["ingredients"]["milk"]
    coffee = resource["coffee"] - MENU[coffee]["ingredients"]["coffee"]
    resource = {
        "water": water,
        "milk": milk,
        "coffee": coffee,
    }
    return resource


def coffee_maker(machine_resources):
    income = 0
    is_machine_on = True
    while is_machine_on:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if prompt == 'off':
            is_machine_on = False
        elif prompt == 'report':
            report(income,machine_resources)
        else:
            resource = resource_manager(prompt,machine_resources)
            if resource == 0:
                coffee_price = coin_processing(prompt)
                if coffee_price != 0:
                    machine_resources = resource_deductor(prompt,machine_resources)
                    print(f"Here is your {prompt} ☕️. Enjoy!")
            else:
                print(resource)


coffee_maker(RESOURCE)