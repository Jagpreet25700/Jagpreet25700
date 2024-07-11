from Coffee_maker_machine import menu , menu_item,CoffeeMaker,MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = menu()

is_on = True


while is_on:
    option = menu.get_item()
    choice = input(f"What would like to have? ({option}):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()    
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.makecoffee(drink)