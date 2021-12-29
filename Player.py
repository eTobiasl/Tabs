class Player:

    def __init__(self, name):
        self.points = 0
        self.name = name
        self.wins = 0
        self.losses = 0

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
        self.points += 500