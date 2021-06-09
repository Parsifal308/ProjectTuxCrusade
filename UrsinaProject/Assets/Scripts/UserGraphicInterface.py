from abc import ABC, abstractmethod

from ursina import *


class IMenu(ABC):
    name = None
    stateVar = None

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def myClick(self, anotherMenu):
        self.stateVar = not self.stateVar
        anotherMenu.stateVar = not anotherMenu.stateVar

    def changeMenu(self, to_Menu):
        self.close()
        to_Menu.open()


# MENU CONFIGURACION
class SettingsMenu(IMenu):
    backButton = None  # Boton volver
    fullscreenButton = None  # Boton pantalla completa
    borderButton = None  # Boton de bordes con o sin
    fpsCounterButton = None  # Contador de fps
    languageButton = None  # idioma

    def __init__(self):
        self.name = 'Menu de configuraciones'
        print(self.name)
        self.stateVar = False
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
        self.languageButton = Button(text='Language',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.085),
                                     position=(0, -0.25))

    def open(self):
        self.backButton.enable()
        self.fullscreenButton.enable()
        self.borderButton.enable()
        self.fpsCounterButton.enable()
        self.languageButton.enable()

    def close(self):
        self.languageButton.disable()
        self.borderButton.disable()
        self.fpsCounterButton.disable()
        self.backButton.disable()
        self.fullscreenButton.disable()


# MENU EN PAUSA
class OnGame(IMenu):
    name = 'Menu de Pausa'
    stateVar = None

    def open(self):
        pass

    def close(self):
        pass


# MENU PRINCIPAL
class MainMenu(IMenu):
    newGameButton = None
    loadGameButton = None
    collectiblesButton = None
    settingsButton = None
    exitGameButton = None

    def __init__(self):
        self.name = 'Menu Principal'
        print(self.name)
        self.stateVar = True
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

    def open(self):
        self.newGameButton.enable()
        self.collectiblesButton.enable()
        self.loadGameButton.enable()
        self.settingsButton.enable()
        self.exitGameButton.enable()

    def close(self):
        self.newGameButton.disable()
        self.collectiblesButton.disable()
        self.loadGameButton.disable()
        self.settingsButton.disable()
        self.exitGameButton.disable()

    def myClick(self, anotherMenu):
        self.stateVar = not self.stateVar
        anotherMenu.stateVar = not anotherMenu.stateVar

class CreateGameMenu(IMenu):

    def open(self):
        pass

    def close(self):
        pass


class CollectibleMenu(IMenu):
    name = 'Menu de desbloqueables'

    def open(self):
        pass

    def close(self):
        pass
