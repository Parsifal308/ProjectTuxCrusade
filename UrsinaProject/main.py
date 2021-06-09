from ursina import *
from Assets.Scripts import AppSystem, UserGraphicInterface, ClassicBoard, ClassicPieces


def startClassicGame(menu):
    camera.position = Vec3(2.5, -15, -15)
    camera.rotation = Vec3(-50, 0, 0)
    board = ClassicBoard.classicBoard()
    board.SetBoard()
    board.SetPieces()
    menu.stateVar = False

tuxCrusadeApp = Ursina() # SE DEFINE LA APP
# ----------------------------------------------------------------------------------------------
appWindow = AppSystem.appWindows()

camera.position = Vec3(0, 0, 0)
camera.rotation = Vec3(0, 0, 0)

mainMenu = UserGraphicInterface.MainMenu()
settingsMenu = UserGraphicInterface.SettingsMenu()
pauseMenu = UserGraphicInterface.OnGame()
newGameMenu = UserGraphicInterface.CreateGameMenu()
collectibleMenu = UserGraphicInterface.CollectibleMenu()
settingsMenu.close()
pauseMenu.close()
newGameMenu.close()
collectibleMenu.close()

mainMenu.settingsButton.on_click = Func(mainMenu.myClick, settingsMenu)
mainMenu.newGameButton.on_click = Func(mainMenu.myClick, newGameMenu)
mainMenu.collectiblesButton.on_click = Func(mainMenu.myClick, collectibleMenu)
mainMenu.exitGameButton.on_click = Func(sys.exit)

settingsMenu.backButton.on_click = Func(settingsMenu.myClick, mainMenu)
collectibleMenu.backButton.on_click = Func(collectibleMenu.myClick, mainMenu)
newGameMenu.backButton.on_click = Func(newGameMenu.myClick, mainMenu)
newGameMenu.startGameButton.on_click = Func(startClassicGame, newGameMenu)

def update():

    if mainMenu.stateVar:
        mainMenu.open()
    else:
        mainMenu.close()
    if settingsMenu.stateVar:
        settingsMenu.open()
    else:
        settingsMenu.close()
    if collectibleMenu.stateVar:
        collectibleMenu.open()
    else:
        collectibleMenu.close()
    if newGameMenu.stateVar:
        newGameMenu.open()
    else:
        newGameMenu.close()

# ----------------------------------------------------------------------------------------------
tuxCrusadeApp.run()  # SE EJECUTA LA APP
