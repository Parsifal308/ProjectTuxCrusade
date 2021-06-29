from ursina import *
from Assets.Scripts import ClassicBoard
from Assets.Scripts.ClassicPieces import pieces
import numpy

global whiteTurn
global cameraParent
global board

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

def selectedPieces(number):
    modelo=pieces.get("modeloBasico")
    textura=pieces.get("textura")
    color=pieces.get("color")

    if (number==11):
        modelo.update({"KingW":""})
        pieces.update({"modeloBasico":modelo})
        print("Linux King Selected")
    elif (number==12):
        modelo.update({"QueenW":""})
        pieces.update({"modeloBasico":modelo})
        print("Linux Queen Selected")
    elif (number == 13):
        modelo.update({"BishopW":""})
        pieces.update({"modeloBasico":modelo})
        print("Linux Bishop Selected")
    elif (number == 14):
        modelo.update({"KnightW":""})
        pieces.update({"modeloBasico":modelo})
        print("Linux Knight Selected")
    elif (number == 15):
        modelo.update({"RookW":""})
        pieces.update({"modeloBasico":modelo})
        print("Linux Rook Selected")
    elif (number == 16):
        modelo.update({"PawnW":""})
        pieces.update({"modeloBasico":modelo})
        print("Linux Pawn Selected")
    elif (number == 21):
        modelo.update({"KingB":""})
        pieces.update({"modeloBasico":modelo})
        print("Windows King Selected")
    elif (number == 22):
        modelo.update({"QueenB":""})
        pieces.update({"modeloBasico":modelo})
        print("Windows Queen Selected")
    elif (number == 23):
        modelo.update({"BishopB":""})
        pieces.update({"modeloBasico":modelo})
        print("Windows Bishop Selected")
    elif (number == 24):
        modelo.update({"KnightB":""})
        pieces.update({"modeloBasico":modelo})
        print("Windows Knight Selected")
    elif (number == 25):
        modelo.update({"RookB":""})
        pieces.update({"modeloBasico":modelo})
        print("Windows Rook Selected")
    elif (number == 26):
        modelo.update({"PawnB":""})
        pieces.update({"modeloBasico":modelo})
        print("Windows Pawn Selected")
