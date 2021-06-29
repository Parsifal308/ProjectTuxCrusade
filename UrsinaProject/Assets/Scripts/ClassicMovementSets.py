from Assets.Scripts import Interfaces


class PawnMovementSet(Interfaces.IMovement):
    name = 'Classic pawn movement set'

    # recibe posicion actual, posicion objetivo, equipo correspondiente, el tablero y retorna TRUE si el movimiento es posible de realizar
    def firstMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board, firstMov):
        if firstMov == True:
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

    def __init__(self):
        self.casilla1 = None  # Primer posicion de la pieza
        self.casilla2 = None  # Segunda posicion de la pieza
        self.color = None  # Se define el color de la pieza

    def move(self):
        # Chequeo donde se ve si las piezas de los reyes y torres mantienen o no su posicion inicial
        self.whiteKing_moved = False
        self.blackKing_moved = False
        self.whiteRook1_moved = False
        self.whiteRook2_moved = False
        self.blackRook1_moved = False
        self.blackRook2_moved = False
        self.enroque = False

    def calculateMovement(self):
        pass

    def basicMovement(self):  # chequea que entre dos casillas haya libertad de paso/no haya otras piezas
        if self.casilla1[0] == self.casilla2[0]:  # movimiento vertical
            pos1 = min(int(self.casilla1[1]), int(self.casilla2[1]))
            pos2 = max(int(self.casilla1[1]), int(self.casilla2[1]))

            for i in range(pos1 + 1, pos2):
                square_on_path = ""  # SE CHEQUEAN LOS CASILLEROS
                if square_on_path != "":  # OTRA PIEZA
                    # SE INSERTA MOVIMIENTO_PERMITIDO()
                    # SE INSERTA ALIADOS()
                    return False

        elif self.casilla1[1] == self.casilla2[1]:  # movimiento horizontal
            pos1 = min(self.ranks.find(self.casilla1[0]), self.ranks.find(self.casilla2[0]))
            pos2 = max(self.ranks.find(self.casilla1[0]), self.ranks.find(self.casilla2[0]))

            for i in range(pos1 + 1, pos2):
                square_on_path = ""  # SE CHEQUEAN LOS CASILLEROS
                if square_on_path != "":  # OTRA PIEZA
                    # SE INSERTA MOVIMIENTO_PERMITIDO()
                    # SE INSERTA ALIADOS()
                    return False

        def aliados(self):  # chequea que no ataque piezas amigas
            pieza2_color = ""  # CODIGO QUE DEFINA LA SEGUNDA PIEZA
            if self.color == "white" and pieza2_color in self.color == "white":
                return True
            if self.color == "black" and pieza2_color in self.color == "black":
                return True
            else:
                return False

        def movimiento_permitido(
                self):  # Chequea que pueda moverse al casillero deseado (en este caso vertical/horizontal)
            if self.color == "white" or self.color == "black":  # se chequea el color de las piezas
                if (int(self.casilla1[1]) == int(self.casilla2[1]) or self.casilla1[0] == self.casilla2[0]):
                    return True
            return False

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
    name = 'Classic king movement set'

    def __init__(self):
        self.casilla1=None  #Primer posicion de la pieza
        self.casilla2=None  #Segunda posicion de la pieza
        self.color=None     #Se define el color de la pieza

    def calculateMovement(self):
        pass

    def move(self):
        pass
    def basicMovement(self):
        def aliados(self):  # chequea que no ataque piezas amigas
            pieza2_color = ""  # CODIGO QUE DEFINA LA SEGUNDA PIEZA
            if self.color == "white" and pieza2_color in self.color == "white":
                return True
            if self.color == "black" and pieza2_color in self.color == "black":
                return True
            else:
                return False

        def movimiento_permitido(self):  # Chequea que pueda moverse al casillero deseado (en este caso vertical/horizontal)
            if self.color == "white" or self.color == "black":  # se chequea el color de las piezas
                if (int(self.casilla1[1]) == int(self.casilla2[1]) or self.casilla1[0] == self.casilla2[0]):
                    return True
            return False

        if self.casilla1 == (self.color=="white") or self.casilla1 == (self.color=="black"):
            if (abs(int(self.casilla1[1]) - int(self.casilla2[1])) == 2) and (abs(self.ranks.find(self.casilla1[0]) - self.ranks.find(self.casilla2[0])) == 1): #Movimiento de "L Vertical"
                return True
            if (abs(int(self.casilla1[1]) - int(self.casilla2[1])) == 1) and (abs(self.ranks.find(self.casilla1[0]) - self.ranks.find(self.casilla2[0])) == 2): #Movimiento de "L Horizontal"
                return True