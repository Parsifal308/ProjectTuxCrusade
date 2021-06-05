from Interfaces.IBoard import IBoard as board


class classicBoard(board):
    ySize = 8
    xSize = 8
    positions = (xSize, ySize)

    def SetPieces(self):  # settea las piezas para iniciar una partida de la manera original
        pass
