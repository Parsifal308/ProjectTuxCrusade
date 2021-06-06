from abc import ABC, abstractmethod
import numpy
from enum import Enum


class IBehaviour(ABC):
    name = None
    ySize = None
    xSize = None
    positions = (None, None)

    @abstractmethod
    def computeTurn(self):  # calcula cual es el siguiente curso de accion segun el estado del tablero en el momento
        pass


# La base para crear piezas, junto a sus movimientos posibles, etc
class Team(Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    Blue = 3


class IPiece(ABC):
    name = None
    value = None
    team = type(Team)
    behaviour = type(IBehaviour)


class IBoard(ABC):
    name = None
    xSize = None
    ySize = None
    positions = numpy.empty((xSize, ySize), dtype=IPiece)

    @abstractmethod
    def SetPieces(self):  # settea las piezas en el tablero al comienzo del juego
        pass

    @abstractmethod
    def SetBoard(self):  # settea el tablero
        pass
