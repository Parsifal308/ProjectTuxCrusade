from ursina import *


def guardarPartida():
    print('Se debe guardar la partida')


def cargarPartida():
    print('Se debe cargar la partida')


def exitApp():
    sys.exit('Regresa pronto cruzado!!')


class appWindows:
    def __init__(self):
        window.title = 'Tux Crusade'  # El nombre de la ventana
        window.borderless = False  # Mostrar borde
        window.fullscreen = False  # Pantalla completa
        window.exit_button.visible = False  # Show the in-game red X that loses the window
        window.fps_counter.enabled = True  # contador de FPS
        window.color = color.violet
