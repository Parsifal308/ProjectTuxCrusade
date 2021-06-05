from ursina import *
from abc import ABC, abstractmethod
import sys


class IMenu(ABC):
    name = None

    @abstractmethod
    def open(self):
        pass


def exitApp():
    sys.exit('Regresa pronto cruzado!!')


class SettingsMenu(IMenu):
    name = 'Menu de configuraciones'

    def open(self):
        print('Se debe abrir menu de configuraciones de la app')


class OnGame(IMenu):
    name = 'Menu principal durante la partida'

    def open(self):
        print('Se debe abrir un menu dentro de la partida, donde deja guardar, cargar, salir, etc')





class MainMenu(IMenu):
    name = None
    newGameButton = None
    loadGameButton = None
    collectiblesButton = None
    settingsButton = None
    exitGameButton = None

    def __init__(self):
        self.name = 'Creando menu de inicio del juego'
        print(self.name)
        self.newGameButton = Button(text='New Game',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.4, 0.075),
                                    position=(0, 0.35))
        self.newGameButton = Button(text='Collectibles',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.4, 0.075),
                                    position=(0, 0.2))
        self.newGameButton = Button(text='Load Game',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.4, 0.075),
                                    position=(0, 0.05))
        self.newGameButton = Button(text='Settings',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.4, 0.075),
                                    position=(0, -0.15))
        self.exitGameButton = Button(text='Exit',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.075),
                                     position=(0, -0.35))
        self.exitGameButton.on_click = exitApp

    def open(self):
        print('Se debe abrir el menu principal de la app')


class CreateGameMenu(IMenu):
    name = 'Menu de creacion de nueva partida'

    def open(self):
        print('Se debe abrir un menu para crear una nueva partida')


class CollectibleMenu(IMenu):
    name = 'Menu de desbloqueables'

    def open(self):
        print('Se debe abrir un menu para visualizar y seleccionar los objetos desbloqueables')
