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

    def diagonalMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):  # movimiento diagonal
        if team == 'white':
            if (yPosTarget > yPos) and (xPosTarget > xPos):  # va hacia el Sur Este
                cantidadLugaresSE = yPosTarget - yPos
                for i in cantidadLugaresSE:
                    if not board.checkEmptyPosition(xPos + i, yPos + i):
                        return False
                return True
            else:
                if (yPosTarget > yPos) and (xPosTarget < xPos):  # va hacia el Sur Oeste
                    cantidadLugaresSO = yPosTarget - yPos
                    for i in cantidadLugaresSO:
                        if not board.checkEmptyPosition(xPos - i, yPos + i):
                            return False
                    return True
                else:
                    if (yPosTarget < yPos) and (xPosTarget > xPos):  # va hacia el Nor Este
                        cantidadLugaresNE = xPosTarget - xPos
                        for i in cantidadLugaresNE:
                            if not board.checkEmptyPosition(xPos + i, yPos - i):
                                return False
                        return True
                    else:
                        if (yPosTarget < yPos) and (xPosTarget < xPos):  # va hacia el Nor Oeste
                            cantidadLugaresNO = xPos - xPosTarget
                            for i in cantidadLugaresNO:
                                if not board.checkEmptyPosition(xPos - i, yPos - i):
                                    return False
                            return True

        else:
            if team == 'black':
                if (yPosTarget > yPos) and (xPosTarget > xPos):  # va hacia el Sur Este
                    cantidadLugaresSE = yPosTarget - yPos
                    for i in cantidadLugaresSE:
                        if not board.checkEmptyPosition(xPos + i, yPos + i):
                            return False
                    return True
                else:
                    if (yPosTarget > yPos) and (xPosTarget < xPos):  # va hacia el Sur Oeste
                        cantidadLugaresSO = yPosTarget - yPos
                        for i in cantidadLugaresSO:
                            if not board.checkEmptyPosition(xPos - i, yPos + i):
                                return False
                        return True
                    else:
                        if (yPosTarget < yPos) and (xPosTarget > xPos):  # va hacia el Nor Este
                            cantidadLugaresNE = xPosTarget - xPos
                            for i in cantidadLugaresNE:
                                if not board.checkEmptyPosition(xPos + i, yPos - i):
                                    return False
                            return True
                        else:
                            if (yPosTarget < yPos) and (xPosTarget < xPos):  # va hacia el Nor Oeste
                                cantidadLugaresNO = xPos - xPosTarget
                                for i in cantidadLugaresNO:
                                    if not board.checkEmptyPosition(xPos - i, yPos - i):
                                        return False
                                return True


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

    def straightMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):  # movimiento recto
        if team == 'white':
            if(yPosTarget>yPos):  #Retrocediendo
                cantidadLugaresRetro = yPosTarget - yPos
                for i in cantidadLugaresRetro:
                    if not board.checkEmptyPosition(xPos, yPos + i):
                        return False
                return True
            else:
                cantidadLugaresAvanza = yPos - yPosTarget
                for i in cantidadLugaresAvanza:
                    if not board.checkEmptyPosition(xPos, yPos - i):
                        return False
                return True
        else:
            if team == 'black':
                if (yPosTarget > yPos):  # Avanza
                    cantidadLugaresAva = yPosTarget - yPos
                    for i in cantidadLugaresAva:
                        if not board.checkEmptyPosition(xPos, yPos + i):
                            return False
                    return True
                else:
                    cantidadLugaresRe = yPos - yPosTarget
                    for i in cantidadLugaresRe:
                        if not board.checkEmptyPosition(xPos, yPos - i):
                            return False
                    return True


    def diagonalMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):  # movimiento diagonal
        if team == 'white':
            if(yPosTarget>yPos) and (xPosTarget >xPos):  #va hacia el Sur Este
                cantidadLugaresSE = yPosTarget - yPos
                for i in cantidadLugaresSE:
                    if not board.checkEmptyPosition(xPos+i, yPos + i):
                        return False
                return True
            else:
                if (yPosTarget > yPos) and (xPosTarget < xPos):  # va hacia el Sur Oeste
                    cantidadLugaresSO = yPosTarget - yPos
                    for i in cantidadLugaresSO:
                        if not board.checkEmptyPosition(xPos - i, yPos + i):
                            return False
                    return True
                else:
                    if (yPosTarget < yPos) and (xPosTarget > xPos):  # va hacia el Nor Este
                        cantidadLugaresNE = xPosTarget - xPos
                        for i in cantidadLugaresNE:
                            if not board.checkEmptyPosition(xPos + i, yPos - i):
                                return False
                        return True
                    else:
                        if (yPosTarget < yPos) and (xPosTarget < xPos):  # va hacia el Nor Oeste
                            cantidadLugaresNO = xPos -xPosTarget
                            for i in cantidadLugaresNO:
                                if not board.checkEmptyPosition(xPos - i, yPos - i):
                                    return False
                            return True

        else:
            if team == 'black':
                if (yPosTarget > yPos) and (xPosTarget > xPos):  # va hacia el Sur Este
                    cantidadLugaresSE = yPosTarget - yPos
                    for i in cantidadLugaresSE:
                        if not board.checkEmptyPosition(xPos + i, yPos + i):
                            return False
                    return True
                else:
                    if (yPosTarget > yPos) and (xPosTarget < xPos):  # va hacia el Sur Oeste
                        cantidadLugaresSO = yPosTarget - yPos
                        for i in cantidadLugaresSO:
                            if not board.checkEmptyPosition(xPos - i, yPos + i):
                                return False
                        return True
                    else:
                        if (yPosTarget < yPos) and (xPosTarget > xPos):  # va hacia el Nor Este
                            cantidadLugaresNE = xPosTarget - xPos
                            for i in cantidadLugaresNE:
                                if not board.checkEmptyPosition(xPos + i, yPos - i):
                                    return False
                            return True
                        else:
                            if (yPosTarget < yPos) and (xPosTarget < xPos):  # va hacia el Nor Oeste
                                cantidadLugaresNO = xPos - xPosTarget
                                for i in cantidadLugaresNO:
                                    if not board.checkEmptyPosition(xPos - i, yPos - i):
                                        return False
                                return True



class KnightMovementSet(Interfaces.IMovement):
    name = 'Classic knight movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass
