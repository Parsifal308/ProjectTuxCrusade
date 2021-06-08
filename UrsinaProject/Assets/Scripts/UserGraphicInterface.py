from ursina import *
from abc import ABC, abstractmethod
from Assets.Scripts import AppSystem


class IMenu(ABC):
    name = None

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


# MENU CONFIGURACION
class SettingsMenu(IMenu):
    name = 'Menu de configuraciones'
    backButton = None  # Boton volver
    fullscreenButton = None  # Boton pantalla completa
    borderButton = None  # Boton de bordes con o sin
    fpsCounterButton = None  # Contador de fps
    lenguageButton = None  # idioma

    def __init__(self):
        self.name = 'Creando menu de inicio del juego'
        print(self.name)
        self.backButton = Button(text='Back',
                                 text_color=color.white,
                                 color=color.gray,
                                 scale=(0.4, 0.085),
                                 position=(0, 0.35))
        self.fullscreenButton = Button(text='Full Screen',
                                       text_color=color.white,
                                       color=color.gray,
                                       scale=(0.4, 0.085),
                                       position=(0, 0.2))
        self.borderButton = Button(text='Border',
                                   text_color=color.white,
                                   color=color.gray,
                                   scale=(0.4, 0.085),
                                   position=(0, 0.05))
        self.fpsCounterButton = Button(text='FPS Counter',
                                       text_color=color.white,
                                       color=color.gray,
                                       scale=(0.4, 0.085),
                                       position=(0, -0.10))
        self.lenguageButton = Button(text='Lenguage',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.085),
                                     position=(0, -0.25))

    def open(self):
        print('Se debe abrir menu de configuraciones de la app')
        self.backButton.enable()
        self.fullscreenButton.enable()
        self.borderButton.enable()
        self.fpsCounterButton.enable()
        self.lenguageButton.enable()

    def close(self):
        print('Se debe cerrar el menu de configuraciones')
        self.lenguageButton.disable()
        self.borderButton.disable()
        self.fpsCounterButton.disable()
        self.backButton.disable()
        self.fullscreenButton.disable()


# MENU EN PAUSA
class OnGame(IMenu):


    def open(self):
        print('Se debe abrir un menu de pausa dentro de la partida, donde deja guardar, cargar, salir, etc')

    def close(self):
        print('Se debe cerrar el menu de pausa')


# MENU PRINCIPAL
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
        self.collectiblesButton = Button(text='Collectibles',
                                         text_color=color.white,
                                         color=color.gray,
                                         scale=(0.4, 0.075),
                                         position=(0, 0.2))
        self.loadGameButton = Button(text='Load Game',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.075),
                                     position=(0, 0.05))
        self.settingsButton = Button(text='Settings',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.075),
                                     position=(0, -0.15))
        self.exitGameButton = Button(text='Exit',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.075),
                                     position=(0, -0.35))
        self.exitGameButton.on_click = AppSystem.exitApp

    def open(self):
        print('Se debe abrir el menu principal de la app')
        self.newGameButton.enable()
        self.collectiblesButton.enable()
        self.loadGameButton.enable()
        self.settingsButton.enable()
        self.exitGameButton.enable()

    def close(self):
        print('Se debe cerrar el menu principal')
        self.newGameButton.disable()
        self.collectiblesButton.disable()
        self.loadGameButton.disable()
        self.settingsButton.disable()
        self.exitGameButton.disable()


class CreateGameMenu(IMenu):
    name = 'Menu de creacion de nueva partida'

    def open(self):
        print('Se debe abrir un menu para crear una nueva partida')

    def close(self):
        print('Se debe cerrar el menu de creacion de partida')


class CollectibleMenu(IMenu):
    name = 'Menu de desbloqueables'
    kingLinuxButton = None
    queenLinuxButton = None
    towerLinuxButton = None
    horseLinuxButton = None
    pawnLinuxButton = None
    kingWindowButton = None
    queenWindowButton = None
    towerWindowButton = None
    horseWindowButton = None
    pawnWindowButton = None
    backButton = None

    def __init__(self):
        self.name = 'Creando menu de desbloqueables'
        print(self.name)
        self.kingWindowButton = Button(text='King Window',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.4, 0.35))
        self.queenWindowButton = Button(text='Queen Window',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.4, 0.1))
        self.towerWindowButton = Button(text='Tower Window',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.4, -0.15))
        self.horseWindowButton = Button(text='Horse Window',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.4, -0.40))
        self.pawnWindowButton = Button(text='Pawn Window',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.1, 0.35))
        self.kingLinuxButton = Button(text='King Linux',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.7, 0.35))
        self.queenLinuxButton = Button(text='Queen Linux',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.7, 0.1))
        self.towerLinuxButton = Button(text='Tower Linux',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.7, -0.15))
        self.horseLinuxButton = Button(text='Horse Linux',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.7, -0.40))
        self.pawnLinuxButton = Button(text='Pawn Linux',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.2),
                                    position=(-0.1, 0.1))
        self.backButton = Button(text='Back',
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.3, 0.055),
                                    position=(0.5, -0.45))


    def open(self):
        print('Se debe abrir un menu para visualizar y seleccionar los objetos desbloqueables')
        self.backButton.enable()
        self.kingLinuxButton.enable()
        self.queenLinuxButton.enable()
        self.towerLinuxButton.enable()
        self.horseLinuxButton.enable()
        self.pawnLinuxButton.enable()
        self.kingWindowButton.enable()
        self.queenWindowButton.enable()
        self.towerWindowButton.enable()
        self.horseWindowButton.enable()
        self.pawnWindowButton.enable()

    def close(self):
        print('Se debe cerrar el menu de coleccionables')
        self.backButton.disable()
        self.kingLinuxButton.disable()
        self.queenLinuxButton.disable()
        self.towerLinuxButton.disable()
        self.horseLinuxButton.disable()
        self.pawnLinuxButton.disable()
        self.kingWindowButton.disable()
        self.queenWindowButton.disable()
        self.towerWindowButton.disable()
        self.horseWindowButton.disable()
        self.pawnWindowButton.disable()
