class menu_item:
    def __init__(self,name,cost,water,milk,coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {"water":water,"milk":milk,"coffee":coffee,}

class menu:
    def __init__(self):
        self.menu = [
            menu_item(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            menu_item(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            menu_item(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
    def get_item(self):
        option= " "
        for item in self.menu:
            option += f"{item.name}/"
        return option    
    def find_drink(self,order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, you have made a wrong selection") 

class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water" : 300,
            "milk" : 200,
            "coffee":100,
        }
    def report(self):
        print(f"Water:{self.resources['water']}")
        print(f"milk:{self.resources['milk']}")
        print(f"coffee:{self.resources['coffee']}")
    def is_resource_sufficient(self,drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] >  self.resources[item]:
                print("Sorry, Ingredient are not sufficient.")
                can_make = False
            else:
                return can_make
    def makecoffee(self,order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}.enjoy your day!!")     

class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
        

           