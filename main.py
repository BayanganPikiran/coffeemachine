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

resources = {
    "water": 5000,
    "milk": 2000,
    "coffee": 1000,
}

bank = 0


def print_report(available_resources, available_money):
    print(f"Water: {available_resources['water']}ml.")
    print(f"Milk: {available_resources['milk']}ml.")
    print(f"Coffee: {available_resources['coffee']}ml.")
    print(f"Money: ${available_money}0")


def are_resources_sufficient(item_ordered, available_resources):
    needed_resources = item_ordered["ingredients"]
    for item in needed_resources:
        if needed_resources[item] > available_resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        else:
            return True


def process_coins():
    print("Give me your money!")
    total = int(input("How many quarters?\n"))*.25
    total += int(input("How many dimes?\n"))*.1
    total += int(input("How many nickels?\n"))*.05
    total += int(input("How many pennies?\n"))*.01
    return total


def transaction_is_successful(money_input, item_ordered):
    money_needed = item_ordered["cost"]
    if money_input >= money_needed:
        global bank
        bank += money_needed
        if money_input > money_needed:
            customer_change = round(money_input- money_needed, 2)
            print(f"Here's ${customer_change} back in change.")
        return True
    else:
        print("You didn't insert enough money, bozo!.  Go panhandle and come back when you have enough.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Now go burn yourself with it.")


machine_is_on = True
while machine_is_on:
    customer_order = input("What would you like? espresso ($1.50)/ latte ($2.50)/ cappuccino ($3.00)\n")
    if customer_order == "off":
        print("We're closed for business.")
        machine_is_on = False
    elif customer_order == "report":
        print_report(resources, bank)
    else:
        ordered_drink = MENU[customer_order]
        if are_resources_sufficient(ordered_drink, resources):
            money_deposited = process_coins()
            if transaction_is_successful(money_deposited, ordered_drink):
                make_coffee(customer_order, ordered_drink["ingredients"])




