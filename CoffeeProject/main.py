from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

valid_choices = ['espresso', 'latte', 'cappuccino', 'report', 'off']


def print_report():
    """Prints all the resources on the controller """
    for resource in resources:
        print(f"{resource} : {resources[resource]}")


def check_resources(drink):
    """Check if the resources are enough for the drink """
    drink_ingredients = MENU[drink]["ingredients"]

    for drink_ingredient in drink_ingredients:
        if drink_ingredients[drink_ingredient] > resources[drink_ingredient]:
            print(f"sorry there is not enough {drink_ingredient}")
            return False
    return True


def process_coins(drink):
    """Process the coins and return the remaining amount"""
    print('please insert coins')
    quarters = int(input('How many Quarters?: '))
    dimes = int(input('How many Dimes?'))
    nickles = int(input("How many nickles?"))
    pennies = int(input('How many pennies?'))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if MENU[drink]["cost"] > total:
        print("Sorry that's not enough money. Money Refunded")
        return False

    print(f"Here's your change: ${total - MENU[drink]['cost']}")
    recalculate_resources(drink)
    return True


def recalculate_resources(drink):
    """Subtract the resources used in the making the drink """
    global resources
    drink_ingredients = MENU[drink]["ingredients"]

    for drink_ingredient in drink_ingredients:
        resources[drink_ingredient] -= drink_ingredients[drink_ingredient]


while True:
    users_choice = input("What would you like? (espresso/latte/cappuccino) : ")

    if users_choice == 'off':
        break
    if users_choice == 'report':
        print_report()

    if users_choice in valid_choices:
        if check_resources(users_choice):
            if process_coins(users_choice):
                print(f'Here is your {users_choice}')
                print_report()