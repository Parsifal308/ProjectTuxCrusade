from ursina import *
from Assets.Scripts import AppSystem, UserGraphicInterface, ClassicBoard, ClassicPieces


def startClassicGame(menu):
    camera.position = Vec3(2.5, -15, -15)
    camera.rotation = Vec3(-50, 0, 0)
    board = ClassicBoard.classicBoard()
    board.SetBoard()
    board.SetPieces()
    menu.stateVar = False

tuxCrusadeApp = Ursina()  # SE DEFINE LA APP
# ----------------------------------------------------------------------------------------------
appWindow = AppSystem.appWindows()

camera.position = Vec3(0, 0, 0)
camera.rotation = Vec3(0, 0, 0)

mainMenu = UserGraphicInterface.MainMenu()
settingsMenu = UserGraphicInterface.SettingsMenu()

mainMenu.settingsButton.on_click = Func(mainMenu.myClick, settingsMenu)
mainMenu.newGameButton.on_click = Func(startClassicGame, mainMenu)

settingsMenu.backButton.on_click = Func(settingsMenu.myClick, mainMenu)

def update():

    if mainMenu.stateVar:
        mainMenu.open()
    else:
        mainMenu.close()
    if settingsMenu.stateVar:
        settingsMenu.open()
    else:
        settingsMenu.close()

# ----------------------------------------------------------------------------------------------
tuxCrusadeApp.run()  # SE EJECUTA LA APP
