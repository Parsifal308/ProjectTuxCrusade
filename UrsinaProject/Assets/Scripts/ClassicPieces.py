from Assets.Scripts.Interfaces import IPiece
from Assets.Scripts import ClassicMovementSets
from enum import Enum
from ursina import *

pieces = {"modeloBasico":{"Null":None,
                          "PawnW":"Base Pawn.obj",
                          "RookW":"Base Rook.obj",
                          "KnightW":"Base Knight.obj",
                          "BishopW":"Base Bishop.obj",
                          "QueenW":"Base Queen.obj",
                          "KingW":"Base King.obj",
                          "PawnB": "Base Pawn.obj",
                          "RookB": "Base Rook.obj",
                          "KnightB": "Base Knight.obj",
                          "BishopB": "Base Bishop.obj",
                          "QueenB": "Base Queen.obj",
                          "KingB": "Base King.obj"
                          },
          "textura":{"Null":None,
                     "PawnW":"Stone Blocks 01",
                     "RookW": "Stone Blocks 01",
                     "KnightW": "Stone Blocks 01",
                     "BishopW": "Stone Blocks 01",
                     "QueenW": "Stone Blocks 01",
                     "KingW": "Stone Blocks 01",
                     "PawnB": "Dark Stone Wall 01",
                     "RookB": "Dark Stone Wall 01",
                     "KnightB": "Dark Stone Wall 01",
                     "BishopB": "Dark Stone Wall 01",
                     "QueenB": "Dark Stone Wall 01",
                     "KingB": "Dark Stone Wall 01"},
          "colores":{"Null":None,
                   "white":"white",
                   "black":"black",
                   "blue":"blue",
                   "red":"red"}
          }

modelo = pieces.get("modeloBasico")
textura = pieces.get("textura")
colores = pieces.get("colores")

class Pawn(IPiece):
    name = None
    value = None
    entity = None
    firstMovement = True
    moveSet = ClassicMovementSets.PawnMovementSet()

    def setFirstMov(self, state):
        self.firstMovement = state

    def getFirstMov(self):
        return self.firstMovement

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'Pawn'
        self.value = 1
        self.team = team
        if team == 'white':
            self.entity = Entity(model=modelo.get('PawnW'), texture=textura.get('PawnW'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model=modelo.get('PawnB'), texture=textura.get('PawnB'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base Pawn.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base Pawn.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)


class Rook(IPiece):
    name = None
    value = None
    entity = None
    moveSet = ClassicMovementSets.RookMovementSet()

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'Rook'
        self.value = 5
        self.team = team
        if team == 'white':
            self.entity = Entity(model=modelo.get('RookW'), texture=textura.get('RookW'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model=modelo.get('RookB'), texture=textura.get('RookB'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base Rook.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base Rook.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)


class Knight(IPiece):
    name = None
    value = None
    entity = None
    moveSet = ClassicMovementSets.KnightMovementSet()

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'Knight'
        self.value = 3
        self.team = team
        if team == 'white':
            self.entity = Entity(model=modelo.get('KnightW'), texture=textura.get('KnightW'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model=modelo.get('KnightB'), texture=textura.get('KnightB'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base Knight.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base Knight.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)


class Bishop(IPiece):
    name = None
    value = None
    entity = None
    moveSet = ClassicMovementSets.BishopMovementSet()

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'Bishop'
        self.value = 3
        self.team = team
        if team == 'white':
            self.entity = Entity(model=modelo.get('BishopW'), texture=textura.get('BishopW'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model=modelo.get('BishopB'), texture=textura.get('BishopB'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base Bishop.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base Bishop.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)


class Queen(IPiece):
    name = None
    value = None
    entity = None
    moveSet = ClassicMovementSets.QueenMovementSet()

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'Queen'
        self.value = 9
        self.team = team
        if team == 'white':
            self.entity = Entity(model=modelo.get('QueenW'), texture=textura.get('QueenW'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model=modelo.get('QueenB'), texture=textura.get('QueenB'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base Queen.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base Queen.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)


class King(IPiece):
    name = None
    value = None
    entity = None
    moveSet = ClassicMovementSets.KingMovementSet()

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'King'
        self.value = -1
        self.team = team
        if team == 'white':
            self.entity = Entity(model=modelo.get('KingW'), texture=textura.get('KingW'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model=modelo.get('KingB'), texture=textura.get('KingB'), position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base King.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base King.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
