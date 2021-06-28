from ursina import *
from Assets.Scripts import AppSystem, UserGraphicInterface, Game

global mainMenu
global settingsMenu
global pauseMenu
global newGameMenu
global collectibleMenu

def resetCamera():
    camera.position = Vec3(0, 0, 0)
    camera.rotation = Vec3(0, 0, 0)

tuxCrusadeApp = Ursina() # SE DEFINE LA APP
# ----------------------------------------------------------------------------------------------
appWindow = AppSystem.appWindows()

mainMenu= UserGraphicInterface.MainMenu()
settingsMenu = UserGraphicInterface.SettingsMenu()
pauseMenu = UserGraphicInterface.OnGame()
newGameMenu = UserGraphicInterface.CreateGameMenu()
collectibleMenu = UserGraphicInterface.CollectibleMenu()

mainMenu.parent = camera
settingsMenu.parent = camera
pauseMenu.parent = camera
newGameMenu.parent = camera
collectibleMenu.parent = camera

resetCamera()
settingsMenu.close()
pauseMenu.close()
newGameMenu.close()
collectibleMenu.close()

mainMenu.settingsButton.on_click = Func(mainMenu.myClick, settingsMenu)
mainMenu.newGameButton.on_click = Func(mainMenu.myClick, newGameMenu)
mainMenu.collectiblesButton.on_click = Func(mainMenu.myClick, collectibleMenu)
mainMenu.exitGameButton.on_click = Func(sys.exit)
settingsMenu.backButton.on_click = Func(settingsMenu.myClick, mainMenu)
newGameMenu.backButton.on_click = Func(newGameMenu.myClick, mainMenu)
newGameMenu.startGameButton.on_click = Func(Game.startClassicGame, newGameMenu)
collectibleMenu.backButton.on_click = Func(collectibleMenu.myClick, mainMenu)

collectibleMenu.kingLinuxButton.on_click = Func(Game.selectedPieces,11)
collectibleMenu.queenLinuxButton.on_click = Func(Game.selectedPieces,12)
collectibleMenu.bishopLinuxButton.on_click = Func(Game.selectedPieces,13)
collectibleMenu.horseLinuxButton.on_click = Func(Game.selectedPieces,14)
collectibleMenu.towerLinuxButton.on_click = Func(Game.selectedPieces,15)
collectibleMenu.pawnLinuxButton.on_click = Func(Game.selectedPieces,16)
collectibleMenu.kingWindowsButton.on_click = Func(Game.selectedPieces,21)
collectibleMenu.queenWindowsButton.on_click = Func(Game.selectedPieces,22)
collectibleMenu.bishopWindowsButton.on_click = Func(Game.selectedPieces,23)
collectibleMenu.horseWindowsButton.on_click = Func(Game.selectedPieces,24)
collectibleMenu.towerWindowsButton.on_click = Func(Game.selectedPieces,25)
collectibleMenu.pawnWindowsButton.on_click = Func(Game.selectedPieces,26)


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
    if held_keys['d']:
        Game.cameraParent.rotation_z -= 75 * time.dt
    if held_keys['a']:
        Game.cameraParent.rotation_z += 75 * time.dt
# ----------------------------------------------------------------------------------------------
tuxCrusadeApp.run()  # SE EJECUTA LA APP
