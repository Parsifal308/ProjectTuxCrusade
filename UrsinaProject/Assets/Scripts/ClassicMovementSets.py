from Assets.Scripts import Interfaces


class PawnMovementSet(Interfaces.IMovement):
    name = 'Classic pawn movement set'

    # recibe posicion actual, posicion objetivo, equipo correspondiente, el tablero y retorna TRUE si el movimiento es posible de realizar
    def firstMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):
        if team == 'white':
            if (xPosTarget, yPosTarget) == (xPos - 2, yPos):  # si dos casillas enfrente
                if board.checkEmptyPosition(xPosTarget - 1, yPosTarget):  # si no hay nada delante
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
                if (xPosTarget, yPosTarget) == (xPos + 2, yPos):
                    if board.checkEmptyPosition(xPosTarget + 1, yPosTarget):  # si no hay nada delante
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
            if (xPosTarget, yPosTarget) == (xPos - 1, yPos):
                if board.checkEmptyPosition(xPosTarget, yPosTarget):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if team == 'black':
                if (xPosTarget, yPosTarget) == (xPos + 1, yPos):
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


class RookMovementSet(Interfaces.IMovement):
    name = 'Classic rook movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class BishopMovementSet(Interfaces.IMovement):
    name = 'Classic bishop movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class KingMovementSet(Interfaces.IMovement):
    name = 'Classic king movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class QueenMovementSet(Interfaces.IMovement):
    name = 'Classic queen movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class KnightMovementSet(Interfaces.IMovement):
    name = 'Classic knight movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass
