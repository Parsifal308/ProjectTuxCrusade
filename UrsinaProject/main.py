import sys

from ursina import *
from Assets.Scripts import UserGraphicInterface as gui

tuxCrusadeApp = Ursina()  # SE DEFINE LA APP
# ----------------------------------------------------------------------------------------------
window.title = 'Tux Crusade'  # El nombre de la ventana
window.borderless = False  # Mostrar borde
window.fullscreen = False  # Pantalla completa
window.exit_button.visible = False  # Show the in-game red X that loses the window
window.fps_counter.enabled = True  # contador de FPS

x = gui.MainMenu()


# ----------------------------------------------------------------------------------------------
tuxCrusadeApp.run()  # SE EJECUTA LA APP