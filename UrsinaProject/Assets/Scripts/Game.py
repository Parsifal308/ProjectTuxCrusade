from ursina import *
from Assets.Scripts import ClassicBoard,ClassicPieces
import numpy

global whiteTurn
global cameraParent
global board
global music1


cameraParent = Entity(position=(3.5, 3.5, 0))




def startClassicGame(menu):
    whiteTurn = True
    camera.parent = cameraParent
    camera.position= Vec3(-0.8, -17, -14)
    camera.rotation = Vec3(-50, 0, 0)
    board = ClassicBoard.classicBoard()
    board.SetBoard()
    board.SetPieces()
    menu.stateVar = False


    def playTurn():
        if whiteTurn:
            print('WHITE PLAYER TURN')

        else:
            print('BLACK PLAYER TURN')
