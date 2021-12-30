class Unit:

    def __init__(self, name, faction, cost, balance):
        self.name = name
        self.faction = faction
        self.cost = cost
        self.balance = balance

    def getName(self):
        return self.name

    def getFaction(self):
        return self.faction

    def getCost(self):
        return self.cost

    def getBalance(self):
        return self.balance