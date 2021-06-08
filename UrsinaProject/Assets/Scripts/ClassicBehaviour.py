from Interfaces import IBehaviour


class PawnBehaviour(IBehaviour):
    name = 'Classic pawn behaviour'

    def computeTurn(self):
        pass


class RookBehaviour(IBehaviour):
    name = 'Classic rook behaviour'

    def computeTurn(self):
        pass


class knightBehaviour(IBehaviour):
    name = 'Classic knight behaviour'

    def computeTurn(self):
        pass


class BishopBehaviour(IBehaviour):
    name = 'Classic bishop behaviour'

    def computeTurn(self):
        pass


class QueenBehaviour(IBehaviour):
    name = 'Classic queen behaviour'

    def computeTurn(self):
        pass


class KingBehaviour(IBehaviour):
    name = 'Classic king behaviour'

    def computeTurn(self):
        print('')