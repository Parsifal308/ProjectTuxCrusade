from ursina import *

from Assets.Scripts import AppSystem as system
from Assets.Scripts import UserGraphicInterface as gui

tuxCrusadeApp = Ursina()  # SE DEFINE LA APP
# ----------------------------------------------------------------------------------------------

appWindow = system.appWindows()

#x = gui.MainMenu()
#x.open()

x = gui.CreateGameMenu()
#x = gui.SettingsMenu() #testeo(Mantener descomentado)

#x = gui.OnGame()
#x = gui.OnGame()
#x.open()

# ----------------------------------------------------------------------------------------------
tuxCrusadeApp.run()  # SE EJECUTA LA APP