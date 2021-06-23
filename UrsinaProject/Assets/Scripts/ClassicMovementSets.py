from Interfaces import IMovement


class PawnMovementSet(IMovement):
    name = 'Classic pawn movement set'

    # recibe posicion actual, posicion objetivo, equipo correspondiente, el tablero y retorna TRUE si el movimiento es posible de realizar
    def firstMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):
        if team == 'white':
            if (yPosTarget, xPosTarget) == (yPos - 2, xPos):  # si dos casillas enfrente
                if board.checkEmptyPosition(xPosTarget, yPosTarget + 1):  # si no hay nada delante
                    if board.checkEmptyPosition(xPosTarget, yPosTarget):  # si no hay nada en la posicion destino
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            if team == 'black':
                if (yPosTarget, xPosTarget) == (yPos + 2, xPos):
                    if board.checkEmptyPosition(xPosTarget, yPosTarget - 1):  # si no hay nada delante
                        if board.checkEmptyPosition(xPosTarget, yPosTarget):  # si no hay nada en la posicion destino
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def basicMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):
        if team == 'white':
            if (yPosTarget, xPosTarget) == (yPos - 1, xPos):
                if board.checkEmptyPosition(xPosTarget, yPosTarget):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if team == 'black':
                if (yPosTarget, xPosTarget) == (yPos + 1, xPos):
                    if board.checkPosition(xPosTarget, yPosTarget):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def specialMovement(self, xPos, yPos, xPosTarget, yPosTarget, team):

        pass

    def calculateMovement(self):
        pass

    def move(self):
        pass


class RookMovementSet(IMovement):
    name = 'Classic rook movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class BishopMovementSet(IMovement):
    name = 'Classic bishop movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class KingMovementSet(IMovement):
    name = 'Classic king movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class QueenMovementSet(IMovement):
    name = 'Classic queen movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class KnightMovementSet(IMovement):
    name = 'Classic knight movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass
