from ursina import *
from Assets.Scripts import ClassicBoard, ClassicPieces
import numpy

whiteTurn= None
cameraParent = None
board = None
music1 = None


cameraParent = Entity(position=(3.5, 3.5, 0))

def startClassicGame(menu, hud):
    global board
    global whiteTurn
    global cameraParent
    whiteTurn = True
    camera.parent = cameraParent
    camera.position= Vec3(-0.8, -17, -14)
    camera.rotation = Vec3(-50, 0, 0)
    board = ClassicBoard.classicBoard()
    board.SetBoard()
    board.SetPieces()
    menu.stateVar = False
    hud.stateVar = True

def playTurn():
    global whiteTurn
    if whiteTurn:
        print('WHITE PLAYER TURN')

    else:
        print('BLACK PLAYER TURN')
