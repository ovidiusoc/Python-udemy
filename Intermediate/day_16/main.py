from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
menuitems = menu.get_items()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    choice = input(f"What would you like? ({menuitems}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        myChoice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(myChoice):
          print(f"The cost of {choice} is ${myChoice.cost}")
          if money_machine.make_payment(myChoice.cost):
              coffee_maker.make_coffee(myChoice)
