from abc import ABC, abstractmethod
from IBoard import IBoard as board


# Es un comportamiento, huye, sobrevive, ataca, etc.
class IBehaviour(ABC):
    name = None
    board = type(board)

    @abstractmethod
    def computeTurn(self):  # calcula cual es el siguiente curso de accion segun el estado del tablero en el momento
        pass
