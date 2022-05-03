class Coffee:
    water = 0
    milk = 0
    coffee = 0
    cost = 0
    name = ""

    def __init__(self, water, milk, coffee, cost, name):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost
        self.name = name

    def getWater(self):
        return self.water

    def getMilk(self):
        return self.milk

    def getCoffee(self):
        return self.coffee

    def getCost(self):
        return self.cost

    def setWater(self, water):
        self.water = water

    def setMilk(self, milk):
        self.milk = milk

    def setCoffee(self, coffee):
        self.coffee = coffee

    def setCost(self, cost):
        self.cost = cost
