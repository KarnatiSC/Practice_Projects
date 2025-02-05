#
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# cash = 0
#
# def check_resources(coffee):
#     """Checks if enough ingredients are available to make the chosen coffee."""
#     for item in coffee:
#         if coffee[item] > resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#         else:
#             return True
#
# def process_coins():
#     """Asks the user to put in coins and calculates the total amount of coins the user puts in."""
#     print("Please insert coins.\n")
#     quarters = int(input("How many Quarters?: "))
#     dimes = int(input("How many dimes?: "))
#     nickles = int(input("How many nickles?: "))
#     pennies = int(input("How many pennies?: "))
#     return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
#
# def transaction_successful(cost):
#     """Checks if the money from the user is enough to pay for the coffee chosen."""
#     if cost > user_cash:
#         print("Sorry that's not enough money. Money refunded")
#         return False
#     elif cost < user_cash:
#         return True
#
# def make_coffee(coffee):
#     """Utilizes the resources needed to make the coffee"""
#     for item in coffee:
#         resources[item] -= coffee[item]
#
# """The operation of the coffee machine"""
# machine_operation = True
# while machine_operation:
#     order = input("What would you like? (espresso/latte/cappuccino): ")
#     if order == "off":
#         print("The machine is being switched off for maintenance")
#         break
#     elif order == "report":
#         print(f"Here are the ingredients and the money left in the coffee machine.\n"
#               f"Water: {resources['water']}ml\n"
#               f"Milk: {resources['milk']}ml\n"
#               f"Coffee: {resources['coffee']}g\n"
#               f"Money: ${cash}\n")
#         continue
#     else:
#         drink = MENU[order]
#         drink_cost = drink["cost"]
#         resources_sufficient = check_resources(drink["ingredients"])
#         if resources_sufficient:
#             user_cash = process_coins()
#             if transaction_successful(drink_cost):
#                 cash += user_cash
#                 if user_cash > drink_cost:
#                     cash -= (user_cash - drink_cost)
#                     print(f"Here is ${round((user_cash - drink_cost), 2)} in change.")
#                 make_coffee(drink["ingredients"])
#                 print(f"Here is your {order}☕ Enjoy!")
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_operation = True
menu = Menu()
machine = CoffeeMaker()
cash = MoneyMachine()
while machine_operation:

    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if order == "off":
        print("The Machine is being switched off for maintenance.")
        break
    elif order == "report":
        machine.report()
        cash.report()
        continue
    else:
        order_drink = menu.find_drink(order)
        if machine.is_resource_sufficient(order_drink):
            if cash.make_payment(order_drink.cost):
                machine.make_coffee(order_drink)





