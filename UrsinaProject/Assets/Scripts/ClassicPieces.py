from IPiece import IPiece as piece


class Pawn(piece):
    name = 'Classic Pawn'
    value = 1


class Rook(piece):
    name = 'Classic Rook'
    value = 5


class Knight(piece):
    name = 'Classic Knight'
    value = 3


class Bishop(piece):
    name = 'Classic Bishop'
    value = 3


class Queen(piece):
    name = 'Classic Queen'
    value = 9


class King(piece):
    name = 'Classic King'
    value = -1  # El unico valor negativo, asi es facil calcular su valor respecto al resto
