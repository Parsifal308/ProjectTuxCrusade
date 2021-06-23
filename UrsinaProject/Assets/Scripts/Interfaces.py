from abc import ABC, abstractmethod
import numpy
from ursina import *

class IMovement(ABC):

    previousBoard = numpy.empty(shape=(8, 8, 2), dtype=Entity)
    nextBoardState = numpy.empty(shape=(8, 8, 2), dtype=Entity)

class IBehaviour(ABC):
    name = None
    ySize = None
    xSize = None
    currentPosition = (None, None)
    objectivePosition = (None, None)

    @abstractmethod
    def computeTurn(self):  # calcula cual es el siguiente curso de accion segun el estado del tablero en el momento
        pass


# La base para crear piezas
class IPiece(ABC):
    name = ''
    value = None
    team = ''
    moveSet = None

    def getTeam(self):
        return self.team

    def getName(self):
        return self.name

    def getMoveSet(self):
        return self.moveSet

class IBoard(ABC):
    name = None
    xSize = None
    ySize = None
    positions = None

    @abstractmethod
    def SetPieces(self):  # settea las piezas en el tablero al comienzo del juego
        pass

    @abstractmethod
    def SetBoard(self):  # settea el tablero
        pass

    @abstractmethod
    def movePiece(self):
        pass


class IMovement(ABC):
    name = None
    xSize = None
    ySize = None
    currentPosition = (None, None)
    objectivePosition = (None, None)
    previousBoard = numpy.empty(shape=(8, 8, 2), dtype=Entity)
    nextBoardState = numpy.empty(shape=(8, 8, 2), dtype=Entity)

    @abstractmethod
    def calculateMovement(self):
        pass

    @abstractmethod
    def move(self):
        pass
