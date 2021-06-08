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
    languageButton = None  # idioma

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
        self.languageButton = Button(text='Language',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.085),
                                     position=(0, -0.25))

    def open(self):
        print('Se debe abrir menu de configuraciones de la app')

    def close(self):
        print('Se debe cerrar el menu de configuraciones')


# MENU EN PAUSA
class OnGame(IMenu):
    name = 'Menu de pausa'
    saveGameButton = None #Guardar partida
    settingsButton = None #Configuracion dentro de la partida
    exitGameButton = None #Volver al menú de inicio
    backButton = None #Salir del menú de pausa y volver a la partida

    def __init__(self):
        self.name = 'Creando el menú de pausa'
        print(self.name)
        self.saveGameButton = Button(text='Save game',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.085),
                                     position=(0, 0.35))
        self.settingsButton = Button(text='Settings',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.085),
                                     position=(0, 0.2))
        self.exitGameButton = Button(text='Exit game',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.085),
                                     position=(0, 0.05))
        self.backButton = Button(text='Back',
                                 text_color=color.white,
                                 color=color.gray,
                                 scale=(0.4, 0.085),
                                 position=(0, -0.10))

    def open(self):
        print('Se debe abrir un menu de pausa dentro de la partida, donde deja guardar, cargar, salir, etc')
        self.saveGameButton.enable()
        self.settingsButton.enable()
        self.exitGameButton.enable()
        self.backButton.enable()

    def close(self):
        print('Se debe cerrar el menu de pausa')
        self.saveGameButton.disable()
        self.settingsButton.disable()
        self.exitGameButton.disable()
        self.backButton.disable()


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
    difficultyButton = None #Se elige la dificultad
    chooseTeamButton = None #Se elige el equipo/color con que jugar
    versusButton = None #Se elige el contrincante. AI u otro jugador
    gameModeButton = None #Se elige modo de juego
    backButton = None #Se retorna al menu principal

    def __init__(self):

        print(self.name)

        self.difficultyButton = Button(text = 'Choose the difficulty',
                                    text_color = color.white,
                                    color = color.gray,
                                    scale = (0.4, 0.075),
                                    position = (0, 0.35))

        self.chooseTeamButton = Button(text = 'Choose your team',
                                       text_color = color.white,
                                       color = color.gray,
                                       scale = (0.4, 0.075),
                                       position = (0, 0.2))
        self.versusButton = Button(text = 'Choose your challenger',
                                   text_color = color.white,
                                   color = color.gray,
                                   scale = (0.4, 0.075,),
                                   position = (0, 0.05))
        self.gameModeButton = Button (text = 'Choose your game mode',
                                      text_color = color.white,
                                      color = color.gray,
                                      scale = (0.4, 0.075),
                                      position = (0, -0.10))
        self.backButton = Button(text = 'Back to menu',
                                 text_color = color.white,
                                 color = color.gray,
                                 scale = (0.4, 0.075),
                                 position = (0, -0.35))


    def open(self):
        print('Se debe abrir un menu para crear una nueva partida')
        self.difficultyButton.enable()
        self.chooseTeamButton.enable()
        self.versusButton.enable()
        self.gameModeButton.enable()
        self.backButton.enable()
    def close(self):
        print('Se debe cerrar el menu de creacion de partida')
        self.difficultyButton.disable()
        self.chooseTeamButton.disable()
        self.versusButton.disable()
        self.gameModeButton.disable()
        self.backButton.disable()

class CollectibleMenu(IMenu):
    name = 'Menu de desbloqueables'

    def open(self):
        print('Se debe abrir un menu para visualizar y seleccionar los objetos desbloqueables')

    def close(self):
        print('Se debe cerrar el menu de coleccionables')
