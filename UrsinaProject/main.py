import sys

from ursina import *
from Assets.Scripts import UserGraphicInterface as gui
from Assets.Scripts import AppSystem as system

tuxCrusadeApp = Ursina()  # SE DEFINE LA APP
# ----------------------------------------------------------------------------------------------

appWindow = system.appWindows()
x = gui.MainMenu()


# ----------------------------------------------------------------------------------------------
tuxCrusadeApp.run()  # SE EJECUTA LA APP