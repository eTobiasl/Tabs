class Player:

    def __init__(self, name):
        self.points = 0
        self.name = name
        self.wins = 0
        self.losses = 0
        self.faction = None
        self.units = []
        self.reset = False

    def getPoints(self):
        return self.points

    def getName(self):
        return self.name

    def getWins(self):
        return self.wins

    def getLosses(self):
        return self.losses

    def addPoints(self, addedPoints):
        self.points += addedPoints

    def subtractPoints(self, subtractedPoints):
        self.points -= subtractedPoints

    def addWin(self):
        self.wins += 1

    def addLoss(self):
        self.losses += 1
    
    def giveFaction(self, faction):
        self.faction = faction
    
    def resetFaction(self):
        self.faction = None
    
    def getFaction(self):
        return self.faction

    def setUnits(self, unit):
        self.units.append(unit)
    
    def getUnits(self):
        return self.units
    
    def resetUnits(self):
        self.units = []

    def setReset(self, declaration):
        self.reset = declaration

    def getReset(self):
        if self.reset:
            return "can reset"
        else:
            return "can't reset"