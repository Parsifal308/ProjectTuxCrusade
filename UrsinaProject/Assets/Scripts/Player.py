class player():
    name = None
    team = None
    score = 0
    turnsPlayed = 0
    piecesCaptured = 0
    piecesLost = 0
    won = 0
    losses = 0
    whiteTeamGames = 0
    blackTeamGames= 0

    def __init__(self,name, team):
        self.name = name
        self.team = team

    def updateStats(self):
        pass

    def readStats(self):
        pass

    def showStats(self):
        pass
