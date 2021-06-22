from Interfaces import IMovement


class PawnMovementSet(IMovement):
    name = 'Classic pawn movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class RookMovementSet(IMovement):
    name = 'Classic rook movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class BishopMovementSet(IMovement):
    name = 'Classic bishop movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class KingMovementSet(IMovement):
    name = 'Classic king movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class QueenMovementSet(IMovement):
    name = 'Classic queen movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass


class KnightMovementSet(IMovement):
    name = 'Classic knight movement set'

    def calculateMovement(self):
        pass

    def move(self):
        pass
    