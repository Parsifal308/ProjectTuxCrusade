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

    def __init__(self):
        self.xPos=None
        self.yPos = None
        self.xPosTarget = None
        self.yPosTarget = None

        # Chequeo donde se ve si las piezas de los reyes y torres mantienen o no su posicion inicial
        self.whiteKing_moved = False
        self.blackKing_moved = False
        self.whiteRook1_moved = False
        self.whiteRook2_moved = False
        self.blackRook1_moved = False
        self.blackRook2_moved = False
        self.enroque = False

    def basicMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):  # chequea que entre dos casillas haya libertad de paso/no haya otras piezas
        directions=((-1,0),(0,-1),(1,0),(0,1))
        if (team=='white'):
            for d in directions:
                for i in range(1,8):
                    endRow = xPos + d[0]*i
                    endCol = yPos + d[1]*i
                    if 0<=endRow<8 and 0<=endCol<8:
                        if (xPosTarget, yPosTarget) == (endRow, yPos):
                            if (board.checkEmptyPosition(xPosTarget, yPosTarget) == True):  # SE CHEQUEAN LOS CASILLEROS
                                return True
                            else:
                                break
                        elif (xPosTarget, yPosTarget) == (xPos, endCol):
                            if (board.checkEmptyPosition(xPosTarget, yPosTarget) == True):  # SE CHEQUEAN LOS CASILLEROS
                                return True
                            else:
                                break
                    else:
                        break

    def specialMovement(self):  # ENROQUE
        # CODIGO A INCLUIR
        if self.whiteKing_moved == False:  # se chequea que el rey blanco no se haya movido
            if self.whiteRook1_moved == False and self.sq2 == "c1":  # se chequea que la torre izquierda no se haya movido y si se quiere hacer enroque a esa direccion
                # CODIGO QUE CHEQUEE QUE NO HAYA PIEZAS EN MEDIO DEL ENROQUE
                self.enroque = True
                return True
            if self.whiteRook2_moved == False and self.sq2 == "g1":  # se chequea que la torre derecha no se haya movido y si se quiere hacer enroque a esa direccion
                # CODIGO QUE CHEQUEE QUE NO HAYA PIEZAS EN MEDIO DEL ENROQUE
                self.enroque = True
                return True
        if self.blackKing_moved == False:  # se chequea que el rey negro no se haya movido
            if self.blackRook1_moved == False and self.sq2 == "c8":  # se chequea que la torre izquierda no se haya movido y si se quiere hacer enroque a esa direccion
                # CODIGO QUE CHEQUEE QUE NO HAYA PIEZAS EN MEDIO DEL ENROQUE
                self.enroque = True
                return True
            if self.blackRook2_moved == False and self.sq2 == "g8":  # se chequea que la torre derecha no se haya movido y si se quiere hacer enroque a esa direccion
                # CODIGO QUE CHEQUEE QUE NO HAYA PIEZAS EN MEDIO DEL ENROQUE
                self.enroque = True
                return True
        else:  # No hay posibilidad alguna de realizar enroque
            return False

    def move(self):
        pass

    def calculateMovement(self):
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

    def basicMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):
        directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        if (team=='white'):
            for d in directions:
                endRow = xPos + d[0]
                endCol = yPos + d[1]
                if 0<=endRow<8 and 0<=endCol<8:
                    if (xPosTarget, yPosTarget) == (endRow, endCol):
                        if (board.checkEmptyPosition(xPosTarget, yPosTarget) == True):  # SE CHEQUEAN LOS CASILLEROS
                            return True

    def calculateMovement(self):
        pass

    def move(self):
        pass