from ursina import *

from Assets.Scripts import AppSystem as system
from Assets.Scripts import UserGraphicInterface as gui

tuxCrusadeApp = Ursina()  # SE DEFINE LA APP
# ----------------------------------------------------------------------------------------------

appWindow = system.appWindows()

#x = gui.MainMenu()
#x.open()

x = gui.CollectibleMenu()
#x = gui.SettingsMenu() #testeo(Mantener descomentado)


# ----------------------------------------------------------------------------------------------
tuxCrusadeApp.run()  # SE EJECUTA LA APP