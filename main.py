from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    user_order = input(f"What would you like to order? Enter {menu.get_items()} ")
    if user_order == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_order == "off":
        is_on = False
    else:
        ordered_item = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(ordered_item) and money_machine.make_payment(ordered_item.cost):
            coffee_maker.make_coffee(ordered_item)



