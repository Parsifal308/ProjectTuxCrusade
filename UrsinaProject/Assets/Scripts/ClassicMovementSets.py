from Interfaces import IMovement
from ClassicBoard import classicBoard

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

    def __init__(self):
        self.casilla1=None  #Primer posicion de la pieza
        self.casilla2=None  #Segunda posicion de la pieza
        self.color=None     #Se define el color de la pieza

        #Chequeo donde se ve si las piezas de los reyes y torres mantienen o no su posicion inicial
        self.whiteKing_moved = False
        self.blackKing_moved = False
        self.whiteRook1_moved = False
        self.whiteRook2_moved = False
        self.blackRook1_moved = False
        self.blackRook2_moved = False
        self.enroque = False

    def calculateMovement(self):
        pass

    def basicMovement(self): # chequea que entre dos casillas haya libertad de paso/no haya otras piezas
        if self.casilla1[0] == self.casilla2[0]:  # movimiento vertical
            pos1 = min(int(self.casilla1[1]), int(self.casilla2[1]))
            pos2 = max(int(self.casilla1[1]), int(self.casilla2[1]))

            for i in range(pos1 + 1, pos2):
                square_on_path = ""  # SE CHEQUEAN LOS CASILLEROS
                if square_on_path != "":  # OTRA PIEZA
                    #SE INSERTA MOVIMIENTO_PERMITIDO()
                    #SE INSERTA ALIADOS()
                    return False

        elif self.casilla1[1] == self.casilla2[1]:  # movimiento horizontal
            pos1 = min(self.ranks.find(self.casilla1[0]), self.ranks.find(self.casilla2[0]))
            pos2 = max(self.ranks.find(self.casilla1[0]), self.ranks.find(self.casilla2[0]))

            for i in range(pos1 + 1, pos2):
                square_on_path = ""  # SE CHEQUEAN LOS CASILLEROS
                if square_on_path != "":  # OTRA PIEZA
                    #SE INSERTA MOVIMIENTO_PERMITIDO()
                    #SE INSERTA ALIADOS()
                    return False

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

    def specialMovement(self): #ENROQUE
        #CODIGO A INCLUIR
        if self.whiteKing_moved == False: #se chequea que el rey blanco no se haya movido
            if self.whiteRook1_moved == False and self.sq2 == "c1": #se chequea que la torre izquierda no se haya movido y si se quiere hacer enroque a esa direccion
                #CODIGO QUE CHEQUEE QUE NO HAYA PIEZAS EN MEDIO DEL ENROQUE
                self.enroque = True
                return True
            if self.whiteRook2_moved == False and self.sq2 == "g1": #se chequea que la torre derecha no se haya movido y si se quiere hacer enroque a esa direccion
                #CODIGO QUE CHEQUEE QUE NO HAYA PIEZAS EN MEDIO DEL ENROQUE
                self.enroque = True
                return True
        if self.blackKing_moved == False:#se chequea que el rey negro no se haya movido
            if self.blackRook1_moved == False and self.sq2 == "c8":#se chequea que la torre izquierda no se haya movido y si se quiere hacer enroque a esa direccion
                # CODIGO QUE CHEQUEE QUE NO HAYA PIEZAS EN MEDIO DEL ENROQUE
                self.enroque = True
                return True
            if self.blackRook2_moved == False and self.sq2 == "g8":#se chequea que la torre derecha no se haya movido y si se quiere hacer enroque a esa direccion
                # CODIGO QUE CHEQUEE QUE NO HAYA PIEZAS EN MEDIO DEL ENROQUE
                self.enroque = True
                return True
        else: #No hay posibilidad alguna de realizar enroque
            return False

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
