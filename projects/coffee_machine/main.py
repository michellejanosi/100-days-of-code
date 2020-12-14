import os, art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def calculate_resources(user_order):
    for item in MENU[user_order]['ingredients']:
        if MENU[user_order]['ingredients'][item] > resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True


def add_resource():
    resource = input("What would you like to add?: ")
    quantity = int(input(f"How much {resource} would you like to add?: "))

    resources[resource] += quantity

    return f"{resource} added."


def calculate_coins(user_order):
    user_order = MENU[user_order]['cost']
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05

    change = total - user_order

    if change == 0:
        return True
    elif change > 0:
        print(f"Here is your change: ${change}.")
        return True
    else:
        print("Not enough coin. Money refunded.")
        return False

def make_coffee(user_order):
    for item in MENU[user_order]['ingredients']:
        resources[item] -= MENU[user_order]['ingredients'][item]

    print(f"Here is your {user_order}.")
    print(art.coffee)
    print("Enjoy!")

def coffee_machine():
    global profit
    is_machine_on = True
    clear_screen()
    print(art.logo)

    while is_machine_on:
        user_order = input("What would you like? (espresso/latte/cappuccino): ")
        if user_order == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif user_order == 'off':
            is_machine_on = False
        elif user_order == 'add':
            add_resource()
        else:
            if calculate_resources(user_order): 
                cost = MENU[user_order]['cost']
                print(f"That will be ${cost}")
                if calculate_coins(user_order):
                    make_coffee(user_order)
                    profit += cost

coffee_machine()
