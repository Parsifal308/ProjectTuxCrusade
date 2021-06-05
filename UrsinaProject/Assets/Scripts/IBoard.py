from abc import ABC, abstractmethod
from IPiece import IPiece as piece
import numpy


# La base para los tableros, el tamaño, casillas disponibles para ocupar con piezas, etc
class IBoard(ABC):
    name = None
    xSize = None
    ySize = None
    positions = numpy.empty((xSize, ySize), dtype=piece)

    @abstractmethod
    def SetPieces(self):  # settea las piezas en el tablero al comienzo del juego
        pass
