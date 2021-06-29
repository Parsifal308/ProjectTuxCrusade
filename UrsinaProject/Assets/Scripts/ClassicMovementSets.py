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
        validPositionX = xPos
        validPositionY = yPos
        if (team=='white'):
            for d in directions:
                for i in range(1,8):
                    endRow = xPos + d[0]*i
                    endCol = yPos + d[1]*i
                    if 0<=endRow<8 and 0<=endCol<8:
                        if (xPosTarget, yPosTarget) == (xPos, endCol):
                            if (board.checkEmptyPosition(xPosTarget, yPosTarget) == True):  # SE CHEQUEAN LOS CASILLEROS
                                return True
                            elif(board.checkEmptyPosition(xPosTarget, yPosTarget) == False):
                                if not board.checkTeam(xPos, yPos, xPosTarget, yPosTarget):
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                                else:
                                    return False
                            else:
                                break
                    #######################################################################
                        elif (xPosTarget, yPosTarget) == (endRow, yPos):
                            if (board.checkEmptyPosition(xPosTarget, yPosTarget) == True):  # SE CHEQUEAN LOS CASILLEROS
                                return True
                            elif(board.checkEmptyPosition(xPosTarget, yPosTarget) == False):
                                if not board.checkTeam(xPos, yPos, xPosTarget, yPosTarget):
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                                else:
                                    return False
                            else:
                                break

        elif(team!='white'):
            for d in directions:
                for i in range(1,8):
                    endRow = xPos + d[0]*i
                    endCol = yPos + d[1]*i
                    if 0<=endRow<8 and 0<=endCol<8:
                        if (xPosTarget, yPosTarget) == (xPos, endCol):
                            if (board.checkEmptyPosition(xPosTarget, yPosTarget) == True):  # SE CHEQUEAN LOS CASILLEROS
                                return True
                            elif(board.checkEmptyPosition(xPosTarget, yPosTarget) == False):
                                if not board.checkTeam(xPos, yPos, xPosTarget, yPosTarget):
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                                else:
                                    return False
                            else:
                                break
                    #######################################################################
                        elif (xPosTarget, yPosTarget) == (endRow, yPos):
                            if (board.checkEmptyPosition(xPosTarget, yPosTarget) == True):  # SE CHEQUEAN LOS CASILLEROS
                                return True
                            elif(board.checkEmptyPosition(xPosTarget, yPosTarget) == False):
                                if not board.checkTeam(xPos, yPos, xPosTarget, yPosTarget):
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                                else:
                                    return False
                            else:
                                break

        """
                print("SURR")
                cantidadLugaresSur = xPosTarget - xPos
                for i in range(1, cantidadLugaresSur + 1):
                    # entramos si esta ocupado el lugar
                    if not board.checkEmptyPosition(xPos + i, yPos):

                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos + i, yPos):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos + i, yPos):
                            if (xPos + i != xPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                print("Devuelve TRUE SUR")
                return True
        """

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
        difX = abs(xPosTarget - xPos)
        difY = abs(yPosTarget - yPos)
        if team == 'white':
            if (yPosTarget > yPos) and (xPosTarget > xPos) and difX == difY:  # va hacia el Sur Este
                print("VA AL SUR ESTE")
                cantidadLugaresSE = yPosTarget - yPos

                for i in range(1, cantidadLugaresSE + 1):
                    if not board.checkEmptyPosition(xPos + i, yPos + i):
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos + i, yPos + i):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos + i, yPos + i):
                            if (yPos + i != yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                return True
            if (yPosTarget > yPos) and (xPosTarget < xPos) and difX == difY:  # va hacia el NOR este
                print("VA AL NE")
                cantidadLugaresNE = yPosTarget - yPos
                for i in range(1, cantidadLugaresNE + 1):
                    if not board.checkEmptyPosition(xPos - i, yPos + i):
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos - i, yPos + i):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos - i, yPos + i):
                            if (yPos + i != yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                return True

            if (yPosTarget < yPos) and (xPosTarget > xPos) and difX == difY:  # va hacia el Nor OEste
                print("VA AL SUR OESTE")
                cantidadLugaresNE = xPosTarget - xPos
                for i in range(1, cantidadLugaresNE + 1):
                    if not board.checkEmptyPosition(xPos + i, yPos - i):
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos + i, yPos - i):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos + i, yPos - i):
                            if (yPos - i != yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                return True

            if (yPosTarget < yPos) and (xPosTarget < xPos) and difX == difY:  # va hacia el Nor Oeste
                print("VAMOS AL NO")
                cantidadLugaresNO = xPos - xPosTarget
                print(cantidadLugaresNO)
                for i in range(1, cantidadLugaresNO + 1):
                    print("Estamos en el for, i vale:", i)
                    if not board.checkEmptyPosition(xPos - i, yPos - i):
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos - i, yPos - i):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos - i, yPos - i):
                            if (yPos - i != yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                    print("Devuelve TRUE NO")
                return True
            else:
                return False

        else:
            if team == 'black':
                if (yPosTarget > yPos) and (xPosTarget > xPos) and difX == difY:  # va hacia el Sur Este
                    print("VA AL SUR ESTE")
                    cantidadLugaresSE = yPosTarget - yPos

                    for i in range(1, cantidadLugaresSE + 1):
                        if not board.checkEmptyPosition(xPos + i, yPos + i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos + i, yPos + i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos + i, yPos + i):
                                if (yPos + i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    return True
                if (yPosTarget > yPos) and (xPosTarget < xPos) and difX == difY:  # va hacia el NOR este
                    print("VA AL NE")
                    cantidadLugaresNE = yPosTarget - yPos
                    for i in range(1, cantidadLugaresNE + 1):
                        if not board.checkEmptyPosition(xPos - i, yPos + i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos - i, yPos + i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos - i, yPos + i):
                                if (yPos + i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    return True

                if (yPosTarget < yPos) and (xPosTarget > xPos) and difX == difY:  # va hacia el Nor OEste
                    print("VA AL SUR OESTE")
                    cantidadLugaresNE = xPosTarget - xPos
                    for i in range(1, cantidadLugaresNE + 1):
                        if not board.checkEmptyPosition(xPos + i, yPos - i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos + i, yPos - i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos + i, yPos - i):
                                if (yPos - i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    return True

                if (yPosTarget < yPos) and (xPosTarget < xPos) and difX == difY:  # va hacia el Nor Oeste
                    print("VAMOS AL NO")
                    cantidadLugaresNO = xPos - xPosTarget
                    print(cantidadLugaresNO)
                    for i in range(1, cantidadLugaresNO + 1):
                        print("Estamos en el for, i vale:", i)
                        if not board.checkEmptyPosition(xPos - i, yPos - i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos - i, yPos - i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos - i, yPos - i):
                                if (yPos - i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                        print("Devuelve TRUE NO")
                    return True
                else:
                    return False


class KingMovementSet(Interfaces.IMovement):
    name = 'Classic king movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass

    def straightMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):
        if team == 'white':
            if xPosTarget==xPos+1 and yPos == yPosTarget: #SUR
                if not board.checkEmptyPosition(xPos+1, yPos):
                    if board.checkTeam(xPos,yPos,xPos+1,yPos):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos+1, yPos):
                        if (xPos + 1 != xPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            elif(xPosTarget==xPos-1 and yPos == yPosTarget): #NORTE
                if not board.checkEmptyPosition(xPos-1, yPos):
                    if board.checkTeam(xPos, yPos, xPos-1, yPos):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos-1, yPos):
                        if(xPos-1!=xPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos,yPos, xPosTarget,yPosTarget)
                            return True
                return True
            elif (xPosTarget == xPos and yPos-1 == yPosTarget):
                if not board.checkEmptyPosition(xPos, yPos-1):
                    if board.checkTeam(xPos, yPos, xPos, yPos-1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos, yPos-1):
                        if (yPos-1!= yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            elif (xPosTarget == xPos and yPos+1 == yPosTarget):
                if not board.checkEmptyPosition(xPos, yPos+1):
                    if board.checkTeam(xPos, yPos, xPos, yPos+1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos, yPos+1):
                        if (yPos +1!= yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            else:
                return False
        elif team == 'black':
            if xPosTarget == xPos + 1 and yPos == yPosTarget:  # SUR
                if not board.checkEmptyPosition(xPos + 1, yPos):
                    if board.checkTeam(xPos, yPos, xPos + 1, yPos):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos + 1, yPos):
                        if (xPos + 1 != xPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            elif (xPosTarget == xPos - 1 and yPos == yPosTarget):  # NORTE
                if not board.checkEmptyPosition(xPos - 1, yPos):
                    if board.checkTeam(xPos, yPos, xPos - 1, yPos):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos - 1, yPos):
                        if (xPos - 1 != xPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            elif (xPosTarget == xPos and yPos - 1 == yPosTarget):
                if not board.checkEmptyPosition(xPos, yPos - 1):
                    if board.checkTeam(xPos, yPos, xPos, yPos - 1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos, yPos - 1):
                        if (yPos - 1 != yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            elif (xPosTarget == xPos and yPos + 1 == yPosTarget):
                if not board.checkEmptyPosition(xPos, yPos + 1):
                    if board.checkTeam(xPos, yPos, xPos, yPos + 1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos, yPos + 1):
                        if (yPos + 1 != yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            else:
                return False

    def diagonalMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):
        if team == 'white':
            if(yPosTarget == yPos+1) and (xPosTarget ==xPos+1):
                if not board.checkEmptyPosition(xPos+1, yPos + 1):
                    if board.checkTeam(xPos, yPos, xPos+1, yPos + 1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos+1, yPos + 1):
                        if (yPos + 1 != yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            if (yPosTarget == yPos+1) and (xPosTarget == xPos-1):
                    if not board.checkEmptyPosition(xPos - 1, yPos + 1):
                        if board.checkTeam(xPos, yPos, xPos-1, yPos + 1):
                            return False
                        if not board.checkTeam(xPos, yPos, xPos-1, yPos + 1):
                            if (yPos + 1 != yPosTarget):
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                    return True

            if (yPosTarget == yPos-1) and (xPosTarget == xPos+1):
                        if not board.checkEmptyPosition(xPos + 1, yPos - 1):
                            if board.checkTeam(xPos, yPos, xPos+1, yPos - 1):
                                return False
                            if not board.checkTeam(xPos, yPos, xPos+1, yPos - 1):
                                if (yPos - 1 != yPosTarget):
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                        return True

            if (yPosTarget == yPos-1) and (xPosTarget == xPos-1):
                if not board.checkEmptyPosition(xPos - 1, yPos - 1):
                    if board.checkTeam(xPos, yPos, xPos-1, yPos - 1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos-1, yPos - 1):
                        if (yPos - 1 != yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            else:
                return False

        elif team == 'black':
            if (yPosTarget == yPos + 1) and (xPosTarget == xPos + 1):
                if not board.checkEmptyPosition(xPos + 1, yPos + 1):
                    if board.checkTeam(xPos, yPos, xPos + 1, yPos + 1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos + 1, yPos + 1):
                        if (yPos + 1 != yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            if (yPosTarget == yPos + 1) and (xPosTarget == xPos - 1):
                if not board.checkEmptyPosition(xPos - 1, yPos + 1):
                    if board.checkTeam(xPos, yPos, xPos - 1, yPos + 1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos - 1, yPos + 1):
                        if (yPos + 1 != yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True

            if (yPosTarget == yPos - 1) and (xPosTarget == xPos + 1):
                if not board.checkEmptyPosition(xPos + 1, yPos - 1):
                    if board.checkTeam(xPos, yPos, xPos + 1, yPos - 1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos + 1, yPos - 1):
                        if (yPos - 1 != yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True

            if (yPosTarget == yPos - 1) and (xPosTarget == xPos - 1):
                if not board.checkEmptyPosition(xPos - 1, yPos - 1):
                    if board.checkTeam(xPos, yPos, xPos - 1, yPos - 1):
                        return False
                    if not board.checkTeam(xPos, yPos, xPos - 1, yPos - 1):
                        if (yPos - 1 != yPosTarget):
                            return False
                        else:
                            board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                            return True
                return True
            else:
                return False

class QueenMovementSet(Interfaces.IMovement):
    name = 'Classic queen movement set'

    def calculateMovement(self):
        pass

    def move(self):

        pass

    def straightMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):  # movimiento recto
        print("Xinicial: ",xPos,"Yinicial: ", yPos,"xFINAL: ", xPosTarget,"yFinal: ", yPosTarget,"Equipo: ", team, board)
        if team == 'white':
            print("blancoo")
            if xPosTarget>xPos and yPos == yPosTarget:  #va al sur
                print("SURR")
                cantidadLugaresSur = xPosTarget - xPos
                for i in range(1,cantidadLugaresSur+1):
                    #entramos si esta ocupado el lugar
                    if not board.checkEmptyPosition(xPos+i, yPos):

                        #entramos si es del mismo equipo
                        if board.checkTeam(xPos,yPos,xPos+i,yPos):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos+i, yPos):
                            if (xPos + i != xPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                print("Devuelve TRUE SUR")
                return True
            if(xPos>xPosTarget and yPos == yPosTarget):
                cantidadLugaresNorte = xPos - xPosTarget
                for i in range(1,cantidadLugaresNorte+1):
                    print("Estamos en el for DEL DIRECTO, i vale:",i)
                    if not board.checkEmptyPosition(xPos-i, yPos):
                        print("Devuelve FALSEEE")
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos-i, yPos):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos-i, yPos):
                            if(xPos-i!=xPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos,yPos, xPosTarget,yPosTarget)
                                return True
                    print("Devuelve TRUE")
                print("Devuelve TRUE FUERA")
                print("Devuelve TRUE NORTE")
                return True
            if(yPosTarget>yPos and xPos == xPosTarget):  #de costado HACIA EL ESTE
                print("ESTEE")
                cantidadLugaresEste = xPosTarget - xPos
                cantidadLugaresEste = yPosTarget - yPos
                print("Lugares al este: ",cantidadLugaresEste)
                for i in range(1, cantidadLugaresEste + 1):
                    print("Estamos en el for DEL ESTE, i vale:", i)
                    if not board.checkEmptyPosition(xPos, yPos+i):
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos, yPos+i):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos, yPos + i):
                            if (yPos + i != yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                print("Devuelve TRUE ESTE")
                return True
            if(yPos>yPosTarget and xPos == xPosTarget): #DE COSTADO HACIA EL OESTE
                cantidadLugaresOeste = xPos - xPosTarget
                cantidadLugaresOeste = yPos - yPosTarget
                print("costado Oeste : ", cantidadLugaresOeste)
                for i in range(1, cantidadLugaresOeste + 1):
                    print("Estamos en el for DEL DIRECTO, i vale:", i)
                    if not board.checkEmptyPosition(xPos, yPos-i):
                        print("Devuelve FALSEEE")
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos, yPos-i):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos, yPos-i):
                            if (yPos - i != yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                    print("Devuelve TRUE")
                print("Devuelve TRUE FUERA")
                print("Devuelve TRUE OESTE")
                return True
            else:
                return False
        else:
            if team == 'black':
                print("NEGRO")
                if xPosTarget > xPos and yPos == yPosTarget:  # va al sur
                    print("SURR")
                    cantidadLugaresSur = xPosTarget - xPos
                    for i in range(1, cantidadLugaresSur + 1):
                        # entramos si esta ocupado el lugar
                        if not board.checkEmptyPosition(xPos + i, yPos):

                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos + i, yPos):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos + i, yPos):
                                if (xPos + i != xPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    print("Devuelve TRUE SUR")
                    return True
                if (xPos > xPosTarget and yPos == yPosTarget):
                    cantidadLugaresNorte = xPos - xPosTarget
                    print("NORTE : ", cantidadLugaresNorte)
                    for i in range(1, cantidadLugaresNorte + 1):
                        print("Estamos en el for DEL DIRECTO, i vale:", i)
                        if not board.checkEmptyPosition(xPos - i, yPos):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos - i, yPos):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos - i, yPos):
                                if (xPos - i != xPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                        print("Devuelve TRUE")
                    print("Devuelve TRUE NORTE")
                    return True
                if (yPosTarget > yPos and xPos == xPosTarget):  # de costado HACIA EL ESTE
                    print("ESTEE")
                    cantidadLugaresEste = yPosTarget - yPos
                    print("Lugares al este: ", cantidadLugaresEste)
                    for i in range(1, cantidadLugaresEste + 1):
                        print("Estamos en el for DEL ESTE, i vale:", i)
                        if not board.checkEmptyPosition(xPos, yPos + i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos, yPos + i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos, yPos + i):
                                if (yPos + i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    print("Devuelve TRUE ESTE")
                    return True
                if (yPos > yPosTarget and xPos == xPosTarget):  # DE COSTADO HACIA EL OESTE
                    cantidadLugaresOeste = yPos - yPosTarget
                    print("costado Oeste : ", cantidadLugaresOeste)
                    for i in range(1, cantidadLugaresOeste + 1):
                        print("Estamos en el for DEL DIRECTO, i vale:", i)
                        if not board.checkEmptyPosition(xPos, yPos - i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos, yPos - i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos, yPos - i):
                                if (yPos - i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                        print("Devuelve TRUE")
                    print("Devuelve TRUE OESTE")
                    return True
                else:
                    return False


    def diagonalMovement(self, xPos, yPos, xPosTarget, yPosTarget, team, board):  # movimiento diagonal
        print("Xinicial: ",xPos,"Yinicial: ", yPos,"xFINAL: ", xPosTarget,"yFinal: ", yPosTarget,"Equipo: ", team, board)
        difX= abs(xPosTarget-xPos)
        difY=abs(yPosTarget-yPos)
        if team == 'white':
            if(yPosTarget > yPos) and (xPosTarget > xPos) and difX == difY:  #va hacia el Sur Este
                print("VA AL SUR ESTE")
                cantidadLugaresSE = yPosTarget - yPos

                for i in range(1,cantidadLugaresSE+1):
                    if not board.checkEmptyPosition(xPos+i, yPos + i):
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos+i, yPos + i):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos+i, yPos + i):
                            if (yPos + i != yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                return True
            if (yPosTarget > yPos) and (xPosTarget < xPos) and difX == difY:  # va hacia el NOR este
                    print("VA AL NE")
                    cantidadLugaresNE = yPosTarget - yPos
                    for i in range(1,cantidadLugaresNE+1):
                        if not board.checkEmptyPosition(xPos - i, yPos + i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos-i, yPos + i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos-i, yPos + i):
                                if (yPos + i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    return True

            if (yPosTarget < yPos) and (xPosTarget > xPos) and difX == difY:  # va hacia el Nor OEste
                        print("VA AL SUR OESTE")
                        cantidadLugaresNE = xPosTarget - xPos
                        for i in range(1,cantidadLugaresNE+1):
                            if not board.checkEmptyPosition(xPos + i, yPos - i):
                                # entramos si es del mismo equipo
                                if board.checkTeam(xPos, yPos, xPos+i, yPos - i):
                                    print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                    return False
                                if not board.checkTeam(xPos, yPos, xPos+i, yPos - i):
                                    if (yPos - i != yPosTarget):
                                        print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                        return False
                                    else:
                                        board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                        return True
                        return True

            if (yPosTarget < yPos) and (xPosTarget < xPos) and difX == difY:  # va hacia el Nor Oeste
                print("VAMOS AL NO")
                cantidadLugaresNO = xPos -xPosTarget
                print(cantidadLugaresNO)
                for i in range(1,cantidadLugaresNO+1):
                    print("Estamos en el for, i vale:" ,i)
                    if not board.checkEmptyPosition(xPos - i, yPos - i):
                        # entramos si es del mismo equipo
                        if board.checkTeam(xPos, yPos, xPos-i, yPos - i):
                            print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                            return False
                        if not board.checkTeam(xPos, yPos, xPos-i, yPos - i):
                            if (yPos - i != yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                return False
                            else:
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
                    print("Devuelve TRUE NO")
                return True
            else:
                return False

        else:
            if team == 'black':
                if (yPosTarget > yPos) and (xPosTarget > xPos) and difX == difY:  # va hacia el Sur Este
                    print("VA AL SUR ESTE")
                    cantidadLugaresSE = yPosTarget - yPos

                    for i in range(1, cantidadLugaresSE + 1):
                        if not board.checkEmptyPosition(xPos + i, yPos + i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos + i, yPos + i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos + i, yPos + i):
                                if (yPos + i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    return True
                if (yPosTarget > yPos) and (xPosTarget < xPos) and difX == difY:  # va hacia el NOR este
                    print("VA AL NE")
                    cantidadLugaresNE = yPosTarget - yPos
                    for i in range(1, cantidadLugaresNE + 1):
                        if not board.checkEmptyPosition(xPos - i, yPos + i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos - i, yPos + i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos - i, yPos + i):
                                if (yPos + i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    return True

                if (yPosTarget < yPos) and (xPosTarget > xPos) and difX == difY:  # va hacia el Nor OEste
                    print("VA AL SUR OESTE")
                    cantidadLugaresNE = xPosTarget - xPos
                    for i in range(1, cantidadLugaresNE + 1):
                        if not board.checkEmptyPosition(xPos + i, yPos - i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos + i, yPos - i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos + i, yPos - i):
                                if (yPos - i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                    return True

                if (yPosTarget < yPos) and (xPosTarget < xPos) and difX == difY:  # va hacia el Nor Oeste
                    print("VAMOS AL NO")
                    cantidadLugaresNO = xPos - xPosTarget
                    print(cantidadLugaresNO)
                    for i in range(1, cantidadLugaresNO + 1):
                        print("Estamos en el for, i vale:", i)
                        if not board.checkEmptyPosition(xPos - i, yPos - i):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPos - i, yPos - i):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPos - i, yPos - i):
                                if (yPos - i != yPosTarget):
                                    print("NO SE PUEDE MOVER; PIEZA DE OTRO COLOR EN EL MEDIO")
                                    return False
                                else:
                                    board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                    return True
                        print("Devuelve TRUE NO")
                    return True
                else:
                    return False


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
                        elif not board.checkEmptyPosition(xPos, yPos):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPosTarget, yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPosTarget, yPosTarget):
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True
        elif(team!='white'):
            for d in directions:
                endRow = xPos + d[0]
                endCol = yPos + d[1]
                if 0<=endRow<8 and 0<=endCol<8:
                    if (xPosTarget, yPosTarget) == (endRow, endCol):
                        if (board.checkEmptyPosition(xPosTarget, yPosTarget) == True):  # SE CHEQUEAN LOS CASILLEROS
                            return True
                        elif not board.checkEmptyPosition(xPos, yPos):
                            # entramos si es del mismo equipo
                            if board.checkTeam(xPos, yPos, xPosTarget, yPosTarget):
                                print("NO SE PUEDE MOVER; PIEZA DEL MISMO COLOR EN EL MEDIO")
                                return False
                            if not board.checkTeam(xPos, yPos, xPosTarget, yPosTarget):
                                board.capturarPieza(xPos, yPos, xPosTarget, yPosTarget)
                                return True

    def calculateMovement(self):
        pass

    def move(self):
        pass