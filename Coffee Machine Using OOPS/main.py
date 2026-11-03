from operator import indexOf

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
'''a. Check the user’s input to decide what to do next.
   b. The prompt should show every time action has completed, e.g. once the drink is
   dispensed. The prompt should show again to serve the next customer.
'''
execute = True
while(execute):
    options = menu.get_items()
    name = input(f"What would You like ? ({options})")
    if name == "off":
        print("Coffee Machine Turning Off....")
        break
    elif name == "report":
        coffee.report()
        money.report()

    else:
        drink = menu.find_drink(name)
        if coffee.is_resource_sufficient(drink) == False:
            print("Sorry For The Inconvenience , The Machine Is Out of Ingredients!!. ")
            execute = False
        else:
            if not money.make_payment(drink.cost):
                execute = False
            else:
                coffee.make_coffee(drink)
                print(f"Enjoy Your {name}")