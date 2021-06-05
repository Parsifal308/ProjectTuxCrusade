from abc import ABC, abstractproperty
from enum import Enum

from IBehaviour import IBehaviour as behaviour


# La base para crear piezas, junto a sus movimientos posibles, etc
class Team(Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    Blue = 3


class IPiece(ABC):
    name = None
    value = None
    team = Team
    behaviour = behaviour
