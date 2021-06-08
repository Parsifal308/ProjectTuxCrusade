from Assets.Scripts.Interfaces import IPiece
from enum import Enum
from ursina import *


class Pawn(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rotation):
        self.name = 'Classic Pawn'
        self.value = 1
        if team == 'white':
            self.entity = Entity(model='cube', color=color.light_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'black':
            self.entity = Entity(model='cube', color=color.dark_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'blue':
            self.entity = Entity(model='cube', color=color.blue, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'red':
            self.entity = Entity(model='cube', color=color.red, position=vec3Pos, scale=scale, rotation=rotation)


class Rook(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rotation):
        self.name = 'Classic Rook'
        self.value = 5
        if team == 'white':
            self.entity = Entity(model='cube', color=color.light_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'black':
            self.entity = Entity(model='cube', color=color.dark_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'blue':
            self.entity = Entity(model='cube', color=color.blue, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'red':
            self.entity = Entity(model='cube', color=color.red, position=vec3Pos, scale=scale, rotation=rotation)


class Knight(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rotation):
        self.name = 'Classic Knight'
        self.value = 3
        if team == 'white':
            self.entity = Entity(model='cube', color=color.light_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'black':
            self.entity = Entity(model='cube', color=color.dark_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'blue':
            self.entity = Entity(model='cube', color=color.blue, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'red':
            self.entity = Entity(model='cube', color=color.red, position=vec3Pos, scale=scale, rotation=rotation)


class Bishop(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rotation):
        self.name = 'Classic Bishop'
        self.value = 3
        if team == 'white':
            self.entity = Entity(model='cube', color=color.light_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'black':
            self.entity = Entity(model='cube', color=color.dark_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'blue':
            self.entity = Entity(model='cube', color=color.blue, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'red':
            self.entity = Entity(model='cube', color=color.red, position=vec3Pos, scale=scale, rotation=rotation)


class Queen(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rotation):
        self.name = 'Classic Queen'
        self.value = 9
        if team == 'white':
            self.entity = Entity(model='cube', color=color.light_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'black':
            self.entity = Entity(model='cube', color=color.dark_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'blue':
            self.entity = Entity(model='cube', color=color.blue, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'red':
            self.entity = Entity(model='cube', color=color.red, position=vec3Pos, scale=scale, rotation=rotation)


class King(IPiece):
    name = None
    value = None
    entity = None

    def __init__(self, team, vec3Pos, scale, rotation):
        self.name = 'Classic King'
        self.value = -1
        if team == 'white':
            self.entity = Entity(model='cube', color=color.light_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'black':
            self.entity = Entity(model='cube', color=color.dark_gray, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'blue':
            self.entity = Entity(model='cube', color=color.blue, position=vec3Pos, scale=scale, rotation=rotation)
        if team == 'red':
            self.entity = Entity(model='cube', color=color.red, position=vec3Pos, scale=scale, rotation=rotation)
