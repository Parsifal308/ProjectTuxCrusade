from ursina import *
from Assets.Scripts import ClassicBoard, ClassicPieces
from Assets.Scripts.ClassicPieces import pieces
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


def selectedPieces(number):
    modelo = pieces.get("modeloBasico")
    textura = pieces.get("textura")
    color = pieces.get("color")

    if (number == 11):
        modelo.update({"KingW": "King Tux.obj"})
        textura.update({"KingW":"Linux Penguin Texture.png"})
        pieces.update({"modeloBasico": textura})
        pieces.update({"modeloBasico": modelo})
        print("Linux King Selected")
    elif (number == 12):
        modelo.update({"QueenW": "Tux Queen.obj"})
        textura.update({"QueenW":"Linux Penguin Texture.png"})
        pieces.update({"modeloBasico": textura})
        pieces.update({"modeloBasico": modelo})
        print("Linux Queen Selected")
    elif (number == 13):
        modelo.update({"BishopW": "Tux Bishop.obj"})
        textura.update({"BishopW":"Linux Penguin Texture.png"})
        pieces.update({"modeloBasico": textura})
        pieces.update({"modeloBasico": modelo})
        print("Linux Bishop Selected")
    elif (number == 14):
        modelo.update({"KnightW": "Tux Knight.obj"})
        textura.update({"KnightW":"Linux Penguin Texture.png"})
        pieces.update({"modeloBasico": textura})
        pieces.update({"modeloBasico": modelo})
        print("Linux Knight Selected")
    elif (number == 15):
        modelo.update({"RookW": "Tux Rook.obj"})
        textura.update({"RookW":"Linux Penguin Texture.png"})
        pieces.update({"modeloBasico": textura})
        pieces.update({"modeloBasico": modelo})
        print("Linux Rook Selected")
    elif (number == 16):
        modelo.update({"PawnW": "Tux Pawn"})
        textura.update({"PawnW":"Linux Penguin Texture.png"})
        pieces.update({"modeloBasico": textura})
        pieces.update({"modeloBasico": modelo})
        print("Linux Pawn Selected")
    # PARA LAS PIEZAS NEGRAS SE MANTIENE EL MODELO POR DEFECTO AL NO ESTAR LA VERSION WINDOWS DISPONIBLE
    elif (number == 21):
        modelo.update({"KingB": "King Windows.obj"})
        pieces.update({"modeloBasico": modelo})
        print("Windows King Selected")
    elif (number == 22):
        modelo.update({"QueenB": "windows queen.obj"})
        pieces.update({"modeloBasico": modelo})
        print("Windows Queen Selected")
    elif (number == 23):
        modelo.update({"BishopB": "Windows Bishop.obj"})
        pieces.update({"modeloBasico": modelo})
        print("Windows Bishop Selected")
    elif (number == 24):
        modelo.update({"KnightB": "Windows Knight.obj"})
        pieces.update({"modeloBasico": modelo})
        print("Windows Knight Selected")
    elif (number == 25):
        modelo.update({"RookB": "Windows Rook.obj"})
        pieces.update({"modeloBasico": modelo})
        print("Windows Rook Selected")
    elif (number == 26):
        modelo.update({"PawnB": "Windows Pawn.obj"})
        pieces.update({"modeloBasico": modelo})
        print("Windows Pawn Selected")