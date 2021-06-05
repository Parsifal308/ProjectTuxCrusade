from IBehaviour import IBehaviour as behaviour


class PawnBehaviour(behaviour):
    name = 'Classic pawn behaviour'

    def computeTurn(self):
        pass


class RookBehaviour(behaviour):
    name = 'Classic rook behaviour'

    def computeTurn(self):
        pass


class knightBehaviour(behaviour):
    name = 'Classic knight behaviour'

    def computeTurn(self):
        pass


class BishopBehaviour(behaviour):
    name = 'Classic bishop behaviour'

    def computeTurn(self):
        pass


class QueenBehaviour(behaviour):
    name = 'Classic queen behaviour'

    def computeTurn(self):
        pass


class KingBehaviour(behaviour):
    name = 'Classic king behaviour'

    def computeTurn(self):
        print('')
