import sys
import numpy
from ursina import *
from Assets.Scripts import AppSystem

tuxCrusadeApp = Ursina()  # SE DEFINE LA APP
# ----------------------------------------------------------------------------------------------
appWindow = AppSystem.appWindows()
whitePawn1 = Entity(model='cube', color=color.random_color(), position=(1, 0, 0), scale=0.75)
whitePawn2 = Entity(model='cube', color=color.random_color(), position=(1, 1, 0), scale=0.75)
whitePawn3 = Entity(model='cube', color=color.random_color(), position=(1, 2, 0), scale=0.75)
whitePawn4 = Entity(model='cube', color=color.random_color(), position=(1, 3, 0), scale=0.75)
whitePawn5 = Entity(model='cube', color=color.random_color(), position=(1, 4, 0), scale=0.75)
whitePawn6 = Entity(model='cube', color=color.random_color(), position=(1, 5, 0), scale=0.75)
whitePawn7 = Entity(model='cube', color=color.random_color(), position=(1, 6, 0), scale=0.75)
whitePawn8 = Entity(model='cube', color=color.random_color(), position=(1, 7, 0), scale=0.75)

whiteRook1 = Entity(model='cube', color=color.random_color(), position=(0, 0, 0), scale=0.75)
whiteKnight1 = Entity(model='cube', color=color.random_color(), position=(0, 1, 0), scale=0.75)
whiteBishop1 = Entity(model='cube', color=color.random_color(), position=(0, 2, 0), scale=0.75)
whiteKing = Entity(model='cube', color=color.random_color(), position=(0, 3, 0), scale=0.75)
whiteQueen = Entity(model='cube', color=color.random_color(), position=(0, 4, 0), scale=0.75)
whiteBishop2 = Entity(model='cube', color=color.random_color(), position=(0, 5, 0), scale=0.75)
whiteKnight2 = Entity(model='cube', color=color.random_color(), position=(0, 6, 0), scale=0.75)
whiteRook2 = Entity(model='cube', color=color.random_color(), position=(0, 7, 0), scale=0.75)

board_1A = Entity(model='cube', color=color.white, position=(0, 0, 1))
board_2A = Entity(model='cube', color=color.black, position=(1, 0, 1))
board_3A = Entity(model='cube', color=color.white, position=(2, 0, 1))
board_4A = Entity(model='cube', color=color.black, position=(3, 0, 1))
board_5A = Entity(model='cube', color=color.white, position=(4, 0, 1))
board_6A = Entity(model='cube', color=color.black, position=(5, 0, 1))
board_7A = Entity(model='cube', color=color.white, position=(6, 0, 1))
board_8A = Entity(model='cube', color=color.black, position=(7, 0, 1))

board_1B = Entity(model='cube', color=color.black, position=(0, 1, 1))
board_2B = Entity(model='cube', color=color.white, position=(1, 1, 1))
board_3B = Entity(model='cube', color=color.black, position=(2, 1, 1))
board_4B = Entity(model='cube', color=color.white, position=(3, 1, 1))
board_5B = Entity(model='cube', color=color.black, position=(4, 1, 1))
board_6B = Entity(model='cube', color=color.white, position=(5, 1, 1))
board_7B = Entity(model='cube', color=color.black, position=(6, 1, 1))
board_8B = Entity(model='cube', color=color.white, position=(7, 1, 1))

board_1C = Entity(model='cube', color=color.white, position=(0, 2, 1))
board_2C = Entity(model='cube', color=color.black, position=(1, 2, 1))
board_3C = Entity(model='cube', color=color.white, position=(2, 2, 1))
board_4C = Entity(model='cube', color=color.black, position=(3, 2, 1))
board_5C = Entity(model='cube', color=color.white, position=(4, 2, 1))
board_6C = Entity(model='cube', color=color.black, position=(5, 2, 1))
board_7C = Entity(model='cube', color=color.white, position=(6, 2, 1))
board_8C = Entity(model='cube', color=color.black, position=(7, 2, 1))

board_1D = Entity(model='cube', color=color.black, position=(0, 3, 1))
board_2D = Entity(model='cube', color=color.white, position=(1, 3, 1))
board_3D = Entity(model='cube', color=color.black, position=(2, 3, 1))
board_4D = Entity(model='cube', color=color.white, position=(3, 3, 1))
board_5D = Entity(model='cube', color=color.black, position=(4, 3, 1))
board_6D = Entity(model='cube', color=color.white, position=(5, 3, 1))
board_7D = Entity(model='cube', color=color.black, position=(6, 3, 1))
board_8D = Entity(model='cube', color=color.white, position=(7, 3, 1))

board_1E = Entity(model='cube', color=color.white, position=(0, 4, 1))
board_2E = Entity(model='cube', color=color.black, position=(1, 4, 1))
board_3E = Entity(model='cube', color=color.white, position=(2, 4, 1))
board_4E = Entity(model='cube', color=color.black, position=(3, 4, 1))
board_5E = Entity(model='cube', color=color.white, position=(4, 4, 1))
board_6E = Entity(model='cube', color=color.black, position=(5, 4, 1))
board_7E = Entity(model='cube', color=color.white, position=(6, 4, 1))
board_8E = Entity(model='cube', color=color.black, position=(7, 4, 1))

board_1F = Entity(model='cube', color=color.black, position=(0, 5, 1))
board_2F = Entity(model='cube', color=color.white, position=(1, 5, 1))
board_3F = Entity(model='cube', color=color.black, position=(2, 5, 1))
board_4F = Entity(model='cube', color=color.white, position=(3, 5, 1))
board_5F = Entity(model='cube', color=color.black, position=(4, 5, 1))
board_6F = Entity(model='cube', color=color.white, position=(5, 5, 1))
board_7F = Entity(model='cube', color=color.black, position=(6, 5, 1))
board_8F = Entity(model='cube', color=color.white, position=(7, 5, 1))

board_1G = Entity(model='cube', color=color.white, position=(0, 6, 1))
board_2G = Entity(model='cube', color=color.black, position=(1, 6, 1))
board_3G = Entity(model='cube', color=color.white, position=(2, 6, 1))
board_4G = Entity(model='cube', color=color.black, position=(3, 6, 1))
board_5G = Entity(model='cube', color=color.white, position=(4, 6, 1))
board_6G = Entity(model='cube', color=color.black, position=(5, 6, 1))
board_7G = Entity(model='cube', color=color.white, position=(6, 6, 1))
board_8G = Entity(model='cube', color=color.black, position=(7, 6, 1))

board_1H = Entity(model='cube', color=color.black, position=(0, 7, 1))
board_2H = Entity(model='cube', color=color.white, position=(1, 7, 1))
board_3H = Entity(model='cube', color=color.black, position=(2, 7, 1))
board_4H = Entity(model='cube', color=color.white, position=(3, 7, 1))
board_5H = Entity(model='cube', color=color.black, position=(4, 7, 1))
board_6H = Entity(model='cube', color=color.white, position=(5, 7, 1))
board_7H = Entity(model='cube', color=color.black, position=(6, 7, 1))
board_8H = Entity(model='cube', color=color.white, position=(7, 7, 1))

camera.position=Vec3(2.5, -15,-15)
camera.rotation=Vec3(-50, 0, 0)
boardMatrix = [[whitePawn1, whitePawn2, whitePawn3, whitePawn4, whitePawn5, whitePawn6, whitePawn7, whitePawn8]]





# ----------------------------------------------------------------------------------------------
tuxCrusadeApp.run()  # SE EJECUTA LA APP