class CoffeeMachine:
    water = 300
    milk = 200
    coffee = 100
    money = 0.00

    def show_report(self):
        water = self.water
        milk = self.milk
        coffee = self.coffee
        money = self.money
        print("Water : {}ml \n"
              "Milk : {}ml \n"
              "Coffee : {}g \n"
              "Money : ${:.2f}".format(water, milk, coffee, money))

    def check_resources(self,coffee):
        flag = True
        depleatedResource = "sorry we are out of the following ingredients: "
        if coffee.water > self.water:
            flag = False
            depleatedResource = depleatedResource + "water "
        if coffee.milk > self.milk:
            depleatedResource = depleatedResource + "milk "
            flag = False
        if coffee.coffee > self.coffee:
            depleatedResource = depleatedResource + "coffee "
            flag = False
        if flag == 0:
            print(depleatedResource)
        return flag

    def process_coins(self):
        print("enter coins")
        quarters = input("how many quarters")
        dimes = input("how many dimes")
        nickels = input("how many nickels")
        cents = input("how many cents")
        totalMoney = (float(quarters) * 0.25) + (float(dimes) * 0.1) + (float(nickels) * 0.05) + (float(cents) * 0.01)
        return totalMoney

    def transaction_Check(self, money, cost):
        if cost <= money:
            self.money += cost
            change = money - cost
            print("Here is ${:.2f} dollars in change".format(change))
            return True
        else:
            return False

    def make_Coffee(self, coffee):
        self.water -= coffee.water
        self.milk -= coffee.milk
        self.coffee -= coffee.coffee
        self.money += coffee.cost
        print("here is your {} Enjoy!".format(coffee.name))


