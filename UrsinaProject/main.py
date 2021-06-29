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
Game.music1 = Audio('Reloaded Installer 2.mp3', pitch=1, loop=True, autoplay=True)


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
collectibleMenu.backButton.on_click = Func(collectibleMenu.myClick, mainMenu)
newGameMenu.backButton.on_click = Func(newGameMenu.myClick, mainMenu)
newGameMenu.startGameButton.on_click = Func(Game.startClassicGame, newGameMenu)
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
