from ursina import *
from Interfaces import IBoard
import numpy


class classicBoard(IBoard):

    def __init__(self):
        self.ySize = 8
        self.xSize = 8
        self.positions = numpy.empty(shape=(self.xSize, self.ySize, 2), dtype=Entity)

    def SetPieces(self):  # settea las piezas en la parte [x, y, 1] de la matriz
        print('Ubicando las piezas')


    def SetBoard(self):
        print('Construyendo tablero')  # settea las piezas del tablero en la parte [x,y,0] de la matriz
        '''Aca hay que hacer un bucle for, para que recorra toda la parte 0 de la matriz
            y vaya creando y guardando entidades con texturas interpuestas asi para cada
            posicion del tablero, podes hacer raytracing para recuperar info de si esta vacia 
            ,ocupada y por quien'''
