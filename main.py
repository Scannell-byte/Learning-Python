import Coffee
import CoffeeMachine

if __name__ == '__main__':
    coffeeMachine = CoffeeMachine.CoffeeMachine()
    order = ""
    while order != "off":
        order = input("what would you like? (espresso/latte/cappuccino)")
        if order == "report":
            coffeeMachine.show_report()
        if order == "espresso":
            espresso = Coffee.Coffee(50, 0, 18, 1.5, "espresso")
            if coffeeMachine.check_resources(espresso):
                totalMoney = coffeeMachine.process_coins()
                if coffeeMachine.transaction_Check(totalMoney, espresso.getCost()):
                    coffeeMachine.make_Coffee(espresso)
                else:
                    print("not enough money")
        if order == "latte":
            latte = Coffee.Coffee(200, 150, 24, 2.5, "latte")
            if coffeeMachine.check_resources(latte):
                totalMoney = coffeeMachine.process_coins()
                if coffeeMachine.transaction_Check(totalMoney, latte.getCost()):
                    coffeeMachine.make_Coffee(latte)
                else:
                    print("not enough money")
        if order == "cappuccino":
            cappuccino = Coffee.Coffee(200, 150, 24, 3)
            if coffeeMachine.check_resources(cappuccino):
                totalMoney = coffeeMachine.process_coins()
                if coffeeMachine.transaction_Check(totalMoney, cappuccino.getCost()):
                    coffeeMachine.make_Coffee(cappuccino)
                else:
                    print("not enough money")

# TODO 1. prompt user by asking "what would you like? (espresso/latte/cappuccino)" DONE
# TODO 2. turn off the Coffee Machine by entering "off" to the prompt DONE
# TODO 3. print "report" DONE
# TODO 4. check resources sufficient DONE
# TODO 5. Process coins DONE
# TODO 6. Check transaction successful DONE
# TODO 7. make coffee DONE
