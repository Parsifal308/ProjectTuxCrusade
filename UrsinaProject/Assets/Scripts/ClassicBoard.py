from ursina import *
from Assets.Scripts.Interfaces import IBoard
from Assets.Scripts.ClassicPieces import *
import numpy


class classicBoard(IBoard):
    def __init__(self):
        self.ySize = 8
        self.xSize = 8
        self.positions = numpy.empty(shape=(self.xSize, self.ySize, 2), dtype=Entity)

    def SetPieces(self):  # settea las piezas en la parte [x, y, 1] de la matriz
        print('Ubicando las piezas')
        self.positions[1, 0, 1] = Pawn('white', Vec3((1, 0, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 1, 1] = Pawn('white', Vec3((1, 1, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 2, 1] = Pawn('white', Vec3((1, 2, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 3, 1] = Pawn('white', Vec3((1, 3, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 4, 1] = Pawn('white', Vec3((1, 4, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 5, 1] = Pawn('white', Vec3((1, 5, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 6, 1] = Pawn('white', Vec3((1, 6, 0.5)), 0.75, 90, 90, 90)
        self.positions[1, 7, 1] = Pawn('white', Vec3((1, 7, 0.5)), 0.75, 90, 90, 90)

        self.positions[0, 0, 1] = Rook('white', Vec3((0, 0, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 1, 1] = Knight('white', Vec3((0, 1, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 2, 1] = Bishop('white', Vec3((0, 2, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 3, 1] = Queen('white', Vec3((0, 3, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 4, 1] = King('white', Vec3((0, 4, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 5, 1] = Bishop('white', Vec3((0, 5, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 6, 1] = Knight('white', Vec3((0, 6, 0.5)), 0.5, 90, 90, 90)
        self.positions[0, 7, 1] = Rook('white', Vec3((0, 7, 0.5)), 0.5, 90, 90, 90)

        self.positions[6, 0, 1] = Pawn('black', Vec3((6, 0, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 1, 1] = Pawn('black', Vec3((6, 1, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 2, 1] = Pawn('black', Vec3((6, 2, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 3, 1] = Pawn('black', Vec3((6, 3, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 4, 1] = Pawn('black', Vec3((6, 4, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 5, 1] = Pawn('black', Vec3((6, 5, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 6, 1] = Pawn('black', Vec3((6, 6, 0.5)), 0.75, -90, 0, 0)
        self.positions[6, 7, 1] = Pawn('black', Vec3((6, 7, 0.5)), 0.75, -90, 0, 0)

        self.positions[7, 0, 1] = Rook('black', Vec3((7, 0, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 1, 1] = Knight('black', Vec3((7, 1, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 2, 1] = Bishop('black', Vec3((7, 2, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 3, 1] = Queen('black', Vec3((7, 3, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 4, 1] = King('black', Vec3((7, 4, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 5, 1] = Bishop('black', Vec3((7, 5, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 6, 1] = Knight('black', Vec3((7, 6, 0.5)), 0.5, -90, 0, 0)
        self.positions[7, 7, 1] = Rook('black', Vec3((7, 7, 0.5)), 0.5, 0, -90, 0)

    def SetBoard(self):
        print('Construyendo tablero')  # settea las piezas del tablero en la parte [x,y,0] de la matriz
        for i in range(len(self.positions)):
            for j in range(len(self.positions[i])):
                if (j % 2) == 0:
                    if (i % 2) == 0:
                        self.positions[i][j][0] = Entity(model='Board Position.obj', texture='White Rock', collider='box', position=(i, j, 1), rotation_x=-90)
                    else:
                        self.positions[i][j][0] = Entity(model='Board Position.obj', texture='Black Rock 01',collider='box', position=(i, j, 1), rotation_x=-90)
                else:
                    if (i % 2) == 0:
                        self.positions[i][j][0] = Entity(model='Board Position.obj', texture='Black Rock 01',collider='box', position=(i, j, 1), rotation_x=-90)
                    else:
                        self.positions[i][j][0] = Entity(model='Board Position.obj', texture='White Rock',collider='box', position=(i, j, 1), rotation_x=-90)
        Entity(model='Board Sides.obj', texture='Wood', position=(7, 0, 1.01), rotation_x=90)
