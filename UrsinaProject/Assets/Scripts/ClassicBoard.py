import numpy

from Assets.Scripts.ClassicPieces import *
from Assets.Scripts.Interfaces import IBoard


class boardPosition(Button):
    selected = False
    xIndex = None
    yIndex = None

    def __init__(self, position=(0, 0, 0), xRotation=0, texture=None, xPos=0, yPos=0):
        super().__init__(
            parent=scene,
            model='Board Position.obj',
            texture=texture,
            color=color.white,
            position=position,
            rotation_x=xRotation,
        )
        self.xIndex = xPos
        self.yIndex = yPos

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print("\nPOSICION DE LA MATRIZ: " + str(self.xIndex) + "." + str(self.yIndex))
                if self.parent.positions[self.xIndex, self.yIndex, 1] is not None:
                    print("EN ESTA POSICION SE ENCUENTRA: " + self.parent.positions[self.xIndex, self.yIndex, 1].name)
                else:
                    print("ESTA POSICION SE ENCUENTRA VACIA :(")
                if not self.parent.pieceSelected:  # si no hay nada selecionado

                    if not self.parent.checkEmptyPosition(self.xIndex, self.yIndex):  # si no esta vacio

                        if self.parent.positions[self.xIndex, self.yIndex, 1].getTeam() == 'white' and self.parent.whiteTurn == 'white':  # es una pieza blanca y es el turno blanco
                            print('JUGADOR BLANCO ESTA A PUNTO DE MOVER PIEZA')
                            self.parent.pieceSelected = True
                            self.parent.selectedPosition = (self.xIndex, self.yIndex)
                            self.color = color.azure

                        elif self.parent.positions[self.xIndex, self.yIndex, 1].getTeam() == 'black' and not self.parent.whiteTurn == 'white':  # es una pieza negra y no es el turno blanco
                            print('JUGADOR NEGRO ESTA A PUNTO DE MOVER PIEZA')
                            self.parent.pieceSelected = True
                            self.parent.selectedPosition = (self.xIndex, self.yIndex)
                            self.color = color.azure

                    else:
                        print("NO HAY NINGUNA PIEZA EN LA POSICION SELECIONADA")  # si se seleciona una posicion vacia
                        print(self.parent.positions[self.xIndex][self.yIndex][1])

                elif self.parent.selectedPosition == (self.xIndex, self.yIndex):  # si ya hay una pieza selecionada y se vuelve a selecionar
                    self.parent.pieceSelected = False
                    self.parent.selectedPosition = None
                    self.color = color.white

                elif self.parent.pieceSelected != (self.xIndex, self.yIndex):  # si hay una pieza seleccionada y se seleciona una posicion diferente

                    if self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getName() == 'Pawn':

                        if self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getMoveSet().firstMovement(self.parent.selectedPosition[0], self.parent.selectedPosition[1], self.xIndex, self.yIndex, self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getTeam(), self.parent, self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getFirstMov()):

                            print("ES POSIBLE REALIZAR EL MOVIMIENTO ESPECIAL INICIAL")
                            self.parent.saveTurn(self.parent.positions[self.parent.selectedPosition[0]][self.parent.selectedPosition[1]][1].getID(),self.parent.positions[self.parent.selectedPosition[0]][self.parent.selectedPosition[1]][1].getTeam(),self.parent.positions[self.parent.selectedPosition[0]][self.parent.selectedPosition[1]][1].getName(), self.xIndex, self.yIndex)
                            self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].setFirstMov(False)
                            self.parent.movePiece(self.parent.selectedPosition[0], self.parent.selectedPosition[1], self.xIndex, self.yIndex)

                        elif self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getMoveSet().basicMovement(self.parent.selectedPosition[0], self.parent.selectedPosition[1], self.xIndex, self.yIndex, self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getTeam(), self.parent):
                            print("ES POSIBLE REALIZAR EL MOVIMIENTO NORMAL")
                            self.parent.saveTurn(self.parent.positions[self.parent.selectedPosition[0]][self.parent.selectedPosition[1]][1].getID(), self.parent.positions[self.parent.selectedPosition[0]][self.parent.selectedPosition[1]][1].getTeam(), self.parent.positions[self.parent.selectedPosition[0]][self.parent.selectedPosition[1]][1].getName(), self.xIndex, self.yIndex)
                            self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].setFirstMov(False)
                            self.parent.movePiece(self.parent.selectedPosition[0], self.parent.selectedPosition[1], self.xIndex, self.yIndex)

                        else:
                            print("MOVIMIENTO NO PERMITIDO")

                    elif self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getName() == 'Rook':
                        print("si intento mover una torre a algun lado....")
                        # aca iria el checkeo con los metodos de la clase moveset

                    elif self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getName() == 'Bishop':
                        print("si intento mover un alfil a algun lado....")
                        # aca iria el checkeo con los metodos de la clase moveset

                    elif self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getName() == 'Knight':
                        print("si intento mover un caballo a algun lado....")
                        # aca iria el checkeo con los metodos de la clase moveset

                    elif self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getName() == 'Queen':
                        print("si intento mover la reina a algun lado....")
                        # aca iria el checkeo con los metodos de la clase moveset

                    elif self.parent.positions[self.parent.selectedPosition[0], self.parent.selectedPosition[1], 1].getName() == 'King':
                        print("si intento mover el Rey a algun lado....")
                        # aca iria el checkeo con los metodos de la clase moveset


class classicBoard(IBoard):
    movHistory = [[None, None, None, None, None]]
    whiteTurn = 'white'
    selectedPosition = None
    targetPosition = None
    pieceSelected = False
    boardStates = numpy.empty(shape=(8, 8, 2), dtype=Entity)

    def __init__(self):
        self.ySize = 8
        self.xSize = 8
        self.positions = numpy.empty(shape=(self.xSize, self.ySize, 2), dtype=Entity)

    def SetPieces(self):
        print('\nUbicando las piezas')
        self.positions[1, 0, 1] = Pawn('black', Vec3((1, 0, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 1, 1] = Pawn('black', Vec3((1, 1, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 2, 1] = Pawn('black', Vec3((1, 2, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 3, 1] = Pawn('black', Vec3((1, 3, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 4, 1] = Pawn('black', Vec3((1, 4, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 5, 1] = Pawn('black', Vec3((1, 5, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 6, 1] = Pawn('black', Vec3((1, 6, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 7, 1] = Pawn('black', Vec3((1, 7, 0.5)), 0.75, 90, 90, 90)

        self.positions[0, 0, 1] = Rook('black', Vec3((0, 0, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 1, 1] = Knight('black', Vec3((0, 1, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 2, 1] = Bishop('black', Vec3((0, 2, 0.5)), 0.75, 90, 90, 90)
        self.positions[0, 3, 1] = Queen('black', Vec3((0, 3, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 4, 1] = King('black', Vec3((0, 4, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 5, 1] = Bishop('black', Vec3((0, 5, 0.5)), 0.75, 90, 90, 90)
        self.positions[0, 6, 1] = Knight('black', Vec3((0, 6, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 7, 1] = Rook('black', Vec3((0, 7, 0.5)), 0.5, 90, 90, 90)

        self.positions[6, 0, 1] = Pawn('white', Vec3((6, 0, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 1, 1] = Pawn('white', Vec3((6, 1, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 2, 1] = Pawn('white', Vec3((6, 2, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 3, 1] = Pawn('white', Vec3((6, 3, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 4, 1] = Pawn('white', Vec3((6, 4, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 5, 1] = Pawn('white', Vec3((6, 5, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 6, 1] = Pawn('white', Vec3((6, 6, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 7, 1] = Pawn('white', Vec3((6, 7, 0.5)), 0.75, -90, 0, 0)

        self.positions[7, 0, 1] = Rook('white', Vec3((7, 0, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 1, 1] = Knight('white', Vec3((7, 1, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 2, 1] = Bishop('white', Vec3((7, 2, 0.5)), 0.75, -90, 0, 0)
        self.positions[7, 3, 1] = Queen('white', Vec3((7, 3, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 4, 1] = King('white', Vec3((7, 4, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 5, 1] = Bishop('white', Vec3((7, 5, 0.5)), 0.75, -90, 0, 0)
        self.positions[7, 6, 1] = Knight('white', Vec3((7, 6, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 7, 1] = Rook('white', Vec3((7, 7, 0.5)), 0.5, -90, 0, 0)

        # SE SETTEAN LAS ID DE LAS PIEZAS
        print('\n')
        for i in range(2):
            for j in range(8):
                self.positions[i][j][1].setID(int( str(i) + str(j) ))
                print("Pieza: " + self.positions[i][j][1].getTeam() + " " + self.positions[i][j][1].getName() + ", ID:  " + str(self.positions[i][j][1].getID()))

        for i in range(6, 8):
            for j in range(8):
                self.positions[i][j][1].setID(int( str(i) + str(j) ))
                print("Pieza: " + self.positions[i][j][1].getTeam() + " " + self.positions[i][j][1].getName() + ", ID:  " + str(self.positions[i][j][1].getID()))

    def SetBoard(self):
        print('\nCONSTRUYENDO TABLERO')  # settea las piezas del tablero en la parte [x,y,0] de la matriz
        for i in range(len(self.positions)):
            for j in range(len(self.positions[i])):
                if (j % 2) == 0:
                    if (i % 2) == 0:
                        self.positions[i][j][0] = boardPosition((i, j, 1), -90, 'defaul white.png', i, j)
                        self.positions[i][j][0].parent = self
                    else:
                        self.positions[i][j][0] = boardPosition((i, j, 1), -90, 'defaul black.png', i, j)
                        self.positions[i][j][0].parent = self
                else:
                    if (i % 2) == 0:
                        self.positions[i][j][0] = boardPosition((i, j, 1), -90, 'defaul black.png', i, j)
                        self.positions[i][j][0].parent = self
                    else:
                        self.positions[i][j][0] = boardPosition((i, j, 1), -90, 'defaul white.png', i, j)
                        self.positions[i][j][0].parent = self
        Entity(model='Board Sides.obj', texture='Wood', position=(7, 0, 1.01), rotation_x=90)

    def checkEmptyPosition(self, xPos, yPos):
        if self.positions[xPos][yPos][1] is None:
            return True
        else:
            return False

    def movePiece(self, xPos, yPos, xTarget, yTarget):
        self.positions[xPos][yPos][1].entity.position = Vec3(xTarget, yTarget, 0.5)
        print("\n--->MOVIENDO MODELO DE PIEZA A POSICION: " + str(xPos) + "." + str(yPos))

        self.positions[xTarget][yTarget][1] = self.positions[xPos][yPos][1]
        print("--->ACTUALIZANDO PIEZA EN MATRIZ, DE: " + str(xPos) +"." + str(yPos) +" HACIA -> " + str(xTarget) +"."+ str(yTarget))

        self.positions[self.selectedPosition[0]][self.selectedPosition[1], 0].color = color.white
        print("--->REINICIANDO COLOR DE POSICION INICIAL: " + str(self.selectedPosition[0]) + "." + str(self.selectedPosition[1]))

        self.pieceSelected = False
        print("--->PIEZA SELECCIONADA: " + str(self.pieceSelected))

        self.positions[xPos][yPos][1] = None
        print("--->POSICION ORGINAL OCUPADA POR: " + str(self.positions[xPos][yPos][1]))
        print("--->POSICION NUEVA OCUPADA POR ID:" + str(self.positions[xTarget][yTarget][1].getID()) + ' ' + str(self.positions[xTarget][yTarget][1].getTeam()) + ' ' + str(self.positions[xTarget][yTarget][1].getName()))

    def saveTurn(self, pieceID, pieceTeam, pieceName, xPos, yPos):
        print('\n')
        turn = [pieceID, pieceTeam, pieceName, xPos, yPos]
        print(turn)
        self.movHistory.append(turn)
        print(self.movHistory)
