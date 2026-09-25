import Data

#TODO 1  Ask Prompt For What would YOu Like
water = Data.resources["water"]
milk = Data.resources["milk"]
coffee = Data.resources["coffee"]
money = 0
coins = 0
machine_on = True
def coinsIn(price):
    print(f"Insert Coins ${price} :- ")
    quarters = int(input("Quarters :"))
    dimes = int(input("Dimes:"))
    nickle = int(input("Nickles :"))
    pennies = int(input("Pennies :"))
    return (quarters*0.25) + (dimes*0.10) + (nickle*0.05) + (pennies*0.01)
Ingredients = True
def enough_ingredients(name):
    global water , milk ,coffee,machine_on
    water -= Data.MENU[name]["ingredients"]["water"]
    milk -= Data.MENU[name]["ingredients"]["milk"]
    coffee -= Data.MENU[name]["ingredients"]["coffee"]
    if(coffee < 0):
        return False
    elif(water<0):
        return False
    elif(milk<0):
        return False
    else:
        return True
def Coffee_Machine(name):
    global water , coffee , machine_on ,money , milk
    if enough_ingredients(name) == True:
        coins = coinsIn(Data.MENU[name]["cost"])
        coins -= Data.MENU[name]["cost"]
        if (coins < 0):
            print("Sorry that's not enough money. Money refunded.")
            machine_on = False
        elif coins > 0:
            print(f"Here is ${round(coins, 2)} Dollars in change.")
            money += Data.MENU[name]["cost"]
        else:
            money += Data.MENU[name]["cost"]

        print(f"Here is Your {name} . Enjoy!!")
    else:
        print("Sorry There isn't Enough Ingredients.")
        machine_on = False


while(machine_on):
    user_input = input("What would you like? espresso/latte/cappuccino):").lower()
    if(user_input == "off"):
        print("Turning Off.....")
        machine_on = False
    elif user_input == "report":
        print(f"Current Resource Available :\n1.Water = {water}\n2.milk ={milk}\n3.coffee = {coffee}\n4.Money = ${money} ")
    elif user_input == "espresso":
        Coffee_Machine("espresso")
    elif user_input == "latte":
        Coffee_Machine("latte")
    elif user_input == "cappuccino":
        Coffee_Machine("cappuccino")
    else:
        print("Sorry Invalid Input")
        print("Please Restart")
        machine_on = False
