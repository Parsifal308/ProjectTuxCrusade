from Assets.Scripts.Interfaces import IPiece
from Assets.Scripts import ClassicMovementSets
from enum import Enum
from ursina import *


class Pawn(IPiece):
    name = None
    value = None
    entity = None
    moveSet = ClassicMovementSets.PawnMovementSet()

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'Pawn'
        self.value = 1
        self.team = team
        if team == 'white':
            self.entity = Entity(model='Base Pawn.obj', texture='Stone Blocks 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model='Base Pawn.obj', texture='Dark Stone Wall 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
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
            self.entity = Entity(model='Base Rook.obj', texture='Stone Blocks 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model='Base Rook.obj', texture='Dark Stone Wall 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
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
            self.entity = Entity(model='Base Knight.obj', texture='Stone Blocks 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model='Base Knight.obj', texture='Dark Stone Wall 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base Knight.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base Knight.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)


class Bishop(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'Bishop'
        self.value = 3
        self.team = team
        if team == 'white':
            self.entity = Entity(model='Base Bishop.obj', texture='Stone Blocks 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model='Base Bishop.obj', texture='Dark Stone Wall 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base Bishop.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base Bishop.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)


class Queen(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'Queen'
        self.value = 9
        self.team = team
        if team == 'white':
            self.entity = Entity(model='Base Queen.obj', texture='Stone Blocks 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model='Base Queen.obj', texture='Dark Stone Wall 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base Queen.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base Queen.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)


class King(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rot_x, rot_y, rot_z):
        self.name = 'King'
        self.value = -1
        self.team = team
        if team == 'white':
            self.entity = Entity(model='Base King.obj', texture='Stone Blocks 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'black':
            self.entity = Entity(model='Base King.obj', texture='Dark Stone Wall 01', position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'blue':
            self.entity = Entity(model='Base King.obj', color=color.blue, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
        if team == 'red':
            self.entity = Entity(model='Base King.obj', color=color.red, position=vec3Pos, scale=scale, rotation_x=rot_x, rotation_y=rot_y, rotation_z=rot_z)
