from Interfaces import IMovement


class PawnMovementSet(IMovement):
    name = 'Classic pawn movement set'

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



class KnightMovementSet(IMovement):
    name = 'Classic knight movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass
