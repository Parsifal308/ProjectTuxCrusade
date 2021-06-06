from Interfaces import IPiece


class Pawn(IPiece):
    name = 'Classic Pawn'
    value = 1


class Rook(IPiece):
    name = 'Classic Rook'
    value = 5


class Knight(IPiece):
    name = 'Classic Knight'
    value = 3


class Bishop(IPiece):
    name = 'Classic Bishop'
    value = 3


class Queen(IPiece):
    name = 'Classic Queen'
    value = 9


class King(IPiece):
    name = 'Classic King'
    value = -1  # El unico valor negativo, asi es facil calcular su valor respecto al resto