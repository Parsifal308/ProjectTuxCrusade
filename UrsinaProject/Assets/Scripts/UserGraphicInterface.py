from ursina import *
from abc import ABC, abstractmethod


class IMenu(ABC):
    name = None
    stateVar = None

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def myClick(self, to_Menu):
        self.stateVar = False
        to_Menu.stateVar = True


# MENU CONFIGURACION
class SettingsMenu(IMenu):
    name = 'Menu de configuraciones'
    backButton = None  # Boton volver
    fullscreenButton = None  # Boton pantalla completa
    borderButton = None  # Boton de bordes con o sin
    fpsCounterButton = None  # Contador de fps
    languageButton = None  # idioma

    def __init__(self):
        self.stateVar = False
        self.backButton = Button(text='Back',
                                 text_color=color.white,
                                 color=color.gray,
                                 scale=(0.4, 0.085),
                                 position=(0, 0.35),
                                 eternal =True)
        self.fullscreenButton = Button(text='Full Screen',
                                       text_color=color.white,
                                       color=color.gray,
                                       scale=(0.4, 0.085),
                                       position=(0, 0.2),
                                       eternal =True)
        self.borderButton = Button(text='Border',
                                   text_color=color.white,
                                   color=color.gray,
                                   scale=(0.4, 0.085),
                                   position=(0, 0.05),
                                   eternal =True)
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
        self.backButton.disable()
        self.fullscreenButton.disable()
        self.borderButton.disable()
        self.fpsCounterButton.disable()
        self.languageButton.disable()


# MENU EN PAUSA
class OnGame(IMenu):
    name = 'Menu de pausa'
    saveGameButton = None  # Guardar partida
    settingsButton = None  # Configuracion dentro de la partida
    exitGameButton = None  # Volver al menú de inicio
    backButton = None  # Salir del menú de pausa y volver a la partida

    def __init__(self):
        self.stateVar = False
        self.saveGameButton = Button(text='Save game',
                                     text_color=color.white,
                                     color=color.dark_gray,
                                     scale=(0.4, 0.085),
                                     position=(0, 0.35),
                                     disabled=True)
        self.settingsButton = Button(text='Settings',
                                     text_color=color.white,
                                     color=color.dark_gray,
                                     scale=(0.4, 0.085),
                                     position=(0, 0.2),
                                     disabled=True)
        self.exitGameButton = Button(text='Exit game',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.085),
                                     position=(0, 0.05))
        self.backButton = Button(text='Resume',
                                 text_color=color.white,
                                 color=color.gray,
                                 scale=(0.4, 0.085),
                                 position=(0, -0.10))

    def open(self):
        self.saveGameButton.enable()
        self.settingsButton.enable()
        self.exitGameButton.enable()
        self.backButton.enable()

    def close(self):
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
    creditsButton = None

    def __init__(self):
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
                                     color=color.dark_gray,
                                     scale=(0.4, 0.075),
                                     position=(0, 0.05),
                                     disabled=True)
        self.settingsButton = Button(text='Settings',
                                     text_color=color.white,
                                     color=color.dark_gray,
                                     scale=(0.4, 0.075),
                                     position=(0, -0.15),
                                     disabled=True)
        self.exitGameButton = Button(text='Exit',
                                     text_color=color.white,
                                     color=color.gray,
                                     scale=(0.4, 0.075),
                                     position=(0, -0.35))
        self.creditsButton = Button(text="Credits",
                                    text_color=color.white,
                                    color=color.gray,
                                    scale=(0.2, 0.05),
                                    position=(0.6, -0.4))

    def open(self):
        self.newGameButton.enable()
        self.collectiblesButton.enable()
        self.loadGameButton.enable()
        self.settingsButton.enable()
        self.exitGameButton.enable()
        self.creditsButton.enable()

    def close(self):
        self.newGameButton.disable()
        self.collectiblesButton.disable()
        self.loadGameButton.disable()
        self.settingsButton.disable()
        self.exitGameButton.disable()
        self.creditsButton.disable()


class CreateGameMenu(IMenu):
    name = 'Menu de creacion de nueva partida'
    startGameButton = None
    difficultyButton = None  # Se elige la dificultad
    chooseTeamButton = None  # Se elige el equipo/color con que jugar
    versusButton = None  # Se elige el contrincante. AI u otro jugador
    gameModeButton = None  # Se elige modo de juego
    backButton = None  # Se retorna al menu principal

    def __init__(self):
        print(self.name)
        self.stateVar = False
        self.startGameButton = Button(text='START GAME!!',
                                      text_color=color.white,
                                      color=color.gray,
                                      scale=(0.4, 0.075),
                                      position=(0, 0.35))
        self.difficultyButton = Button(text='Choose the difficulty',
                                       text_color=color.white,
                                       color=color.dark_gray,
                                       scale=(0.4, 0.075),
                                       position=(0, 0.2),
                                       disabled=True)
        self.chooseTeamButton = Button(text='Choose your team',
                                       text_color=color.white,
                                       color=color.dark_gray,
                                       scale=(0.4, 0.075),
                                       position=(0, 0.1),
                                       disabled=True)
        self.versusButton = Button(text='Choose your challenger',
                                   text_color=color.white,
                                   color=color.dark_gray,
                                   scale=(0.4, 0.075,),
                                   position=(0, 0.),
                                       disabled=True)
        self.gameModeButton = Button(text='Choose your game mode',
                                     text_color=color.white,
                                     color=color.dark_gray,
                                     scale=(0.4, 0.075),
                                     position=(0, -0.1),
                                       disabled=True)
        self.backButton = Button(text='Back to menu',
                                 text_color=color.white,
                                 color=color.gray,
                                 scale=(0.4, 0.075),
                                 position=(0, -0.3))

    def open(self):
        self.difficultyButton.enable()
        self.chooseTeamButton.enable()
        self.versusButton.enable()
        self.gameModeButton.enable()
        self.backButton.enable()
        self.startGameButton.enable()

    def close(self):
        self.difficultyButton.disable()
        self.chooseTeamButton.disable()
        self.versusButton.disable()
        self.gameModeButton.disable()
        self.backButton.disable()
        self.startGameButton.disable()


class CollectibleMenu(IMenu):
    name = 'Menu de desbloqueables'
    kingLinuxButton = None
    queenLinuxButton = None
    towerLinuxButton = None
    horseLinuxButton = None
    pawnLinuxButton = None
    kingWindowsButton = None
    queenWindowsButton = None
    towerWindowsButton = None
    horseWindowsButton = None
    pawnWindowsButton = None
    backButton = None

    def __init__(self):
        self.stateVar = False
        self.kingWindowsButton = Button(text='King Windows',
                                        text_color=color.white,
                                        color=color.gray,
                                        scale=(0.2, 0.2),
                                        position=(-0.4, 0.35))
        self.queenWindowsButton = Button(text='Queen Windows',
                                         text_color=color.white,
                                         color=color.gray,
                                         scale=(0.2, 0.2),
                                         position=(-0.4, 0.1))
        self.towerWindowsButton = Button(text='Tower Windows',
                                         text_color=color.white,
                                         color=color.gray,
                                         scale=(0.2, 0.2),
                                         position=(-0.4, -0.15))
        self.horseWindowsButton = Button(text='Horse Windows',
                                         text_color=color.white,
                                         color=color.gray,
                                         scale=(0.2, 0.2),
                                         position=(-0.4, -0.40))
        self.pawnWindowsButton = Button(text='Pawn Windows',
                                        text_color=color.white,
                                        color=color.gray,
                                        scale=(0.2, 0.2),
                                        position=(-0.1, 0.35))
        self.kingLinuxButton = Button(text_color=color.white,
                                      color=color.white,
                                      scale=(0.2, 0.2),
                                      position=(-0.7, 0.35),
                                      texture='Linux King.png')
        self.queenLinuxButton = Button(text_color=color.white,
                                       color=color.white,
                                       scale=(0.2, 0.2),
                                       position=(-0.7, 0.1),
                                       texture='Linux Queen.png')
        self.towerLinuxButton = Button(text_color=color.white,
                                       color=color.white,
                                       scale=(0.2, 0.2),
                                       position=(-0.7, -0.15),
                                       texture='Linux Rook.png')
        self.horseLinuxButton = Button(text_color=color.white,
                                       color=color.white,
                                       scale=(0.2, 0.2),
                                       position=(-0.7, -0.40),
                                       texture='Linux Knight.png')
        self.pawnLinuxButton = Button(text_color=color.white,
                                      color=color.white,
                                      scale=(0.2, 0.2),
                                      position=(-0.1, 0.1),
                                      texture='Linux Pawn.png')
        self.backButton = Button(text='Back',
                                 text_color=color.white,
                                 color=color.gray,
                                 scale=(0.3, 0.055),
                                 position=(0.5, -0.45))

    def open(self):
        self.backButton.enable()
        self.kingLinuxButton.enable()
        self.queenLinuxButton.enable()
        self.towerLinuxButton.enable()
        self.horseLinuxButton.enable()
        self.pawnLinuxButton.enable()
        self.kingWindowsButton.enable()
        self.queenWindowsButton.enable()
        self.towerWindowsButton.enable()
        self.horseWindowsButton.enable()
        self.pawnWindowsButton.enable()

    def close(self):
        self.backButton.disable()
        self.kingLinuxButton.disable()
        self.queenLinuxButton.disable()
        self.towerLinuxButton.disable()
        self.horseLinuxButton.disable()
        self.pawnLinuxButton.disable()
        self.kingWindowsButton.disable()
        self.queenWindowsButton.disable()
        self.towerWindowsButton.disable()
        self.horseWindowsButton.disable()
        self.pawnWindowsButton.disable()


class creditsMenu(IMenu):
    backButton = None
    ursinaLogo = None
    blenderLogo = None
    name = 'Menu de Creditos'
    text = None
    textCredits = None
    image1 = None
    image2 = None


    def __init__(self):
        self.stateVar = False
        self.textCredits = dedent('''
        <scale:5><black>       CREDITS
        <scale:3><black>              [-----------------------------------------------]
        
        
        <scale:2><black>        Mayra Arevalos [<blue>github.com/Arevalomayra<black>]
        
        <scale:2><black>    Martin Ramirez [<blue>github.com/MartinGR-96<black>]
        
        <scale:2><black>            Guillermo Marinero [<blue>github.com/Parsifal308<black>]
        
        
        <scale:3><black> Made with:                                           
        ''')
        self.text = Text(text=self.textCredits,
                         origin=(0, 0),
                         position=Vec3(-0.1, 0.125, 0),
                         color=color.black,
                         line_height=2)
        self.ursinaLogo = Entity(model='cube',
                                 texture='Ursina2.png',
                                 position=Vec3(-1.25, -1.35, 10),
                                 scale=Vec3(1.6, 1, 0.01),
                                 rotation_x=10,
                                 rotation_y=-1)
        self.blenderLogo = Entity(model='cube',
                                  texture='LogoBlender.png',
                                  position=Vec3(1.25, -1.35, 10),
                                  scale=Vec3(2.5, 1, 0.01),
                                  rotation_x=10,
                                  rotation_y=1)
        self.backButton = Button(text='Back',
                                 text_color=color.white,
                                 color=color.gray,
                                 scale=(0.2, 0.05),
                                 position=(0.75, -0.45))
        self.image1 = Entity(model='cube',
                             texture='Tux King Credit.png',
                             position=Vec3(2.75, 0.5, 10),
                             scale=Vec3(1, 1.5, 0.0001),
                             rotation_z=25)
        self.image2 = Entity(model='cube',
                             texture='Tux Knight Credit.png',
                             position=Vec3(-2.95, 0.5, 10),
                             scale=Vec3(1, 1.5, 0.0001),
                             rotation_z=-25)
    def close(self):
        self.backButton.disable()
        self.blenderLogo.disable()
        self.ursinaLogo.disable()
        self.text.disable()
        self.image1.disable()
        self.image2.disable()

    def open(self):
        self.backButton.enable()
        self.ursinaLogo.enable()
        self.blenderLogo.enable()
        self.text.enable()
        self.image1.enable()
        self.image2.enable()

class onGameHUD(IMenu):
    turn = None
    whiteScore = None
    blackScore = None
    move1 = None
    move2 = None
    move3 = None
    move4 = None
    move5 = None
    helps = None

    def __init__(self):
        self.stateVar = False
        self.turn = Text(text="White Player's Turn",
                         origin=(0, 0),
                         position=Vec3(0, 0.45, 0),
                         color=color.white,
                         line_height=2,
                         scale=2)
        self.whiteScore = Text(text="Score[0]",
                               origin=(0, 0),
                               position=Vec3(0.75, 0.45, 0),
                               color=color.white,
                               line_height=2,
                               scale=2)
        self.blackScore = Text(text="Score[0]",
                               origin=(0, 0),
                               position=Vec3(-0.75, 0.45, 0),
                               color=color.black,
                               line_height=2,
                               scale=2)
        self.helps = Text(text="Press 'A' & 'D' to Rotate",
                               origin=(0, 0),
                               position=Vec3(0.7, -0.475, 0),
                               color=color.black,
                               line_height=2,
                               scale=1)
        self.move1 = Text(text="[1] White Pawn -> box 5.7",
                               origin=(0, 0),
                               position=Vec3(-0.725, -0.475, 0),
                               color=color.black,
                               line_height=2,
                               scale=1)
        self.move2 = Text(text="[2] White Pawn -> box 5.7",
                               origin=(0, 0),
                               position=Vec3(-0.725, -0.425, 0),
                               color=color.black,
                               line_height=2,
                               scale=1)
        self.move3 = Text(text="[3] White Pawn -> box 5.7",
                               origin=(0, 0),
                               position=Vec3(-0.725, -0.375, 0),
                               color=color.black,
                               line_height=2,
                               scale=1)
        self.move4 = Text(text="[4] White Pawn -> box 5.7",
                               origin=(0, 0),
                               position=Vec3(-0.725, -0.325, 0),
                               color=color.black,
                               line_height=2,
                               scale=1)
        self.move5 = Text(text="[5] White Pawn -> box 5.7",
                               origin=(0, 0),
                               position=Vec3(-0.725, -0.275, 0),
                               color=color.black,
                               line_height=2,
                               scale=1)

    def close(self):
        self.turn.disable()
        self.whiteScore.disable()
        self.blackScore.disable()
        self.move1.disable()
        self.move2.disable()
        self.move3.disable()
        self.move4.disable()
        self.move5.disable()
        self.helps.disable()

    def open(self):
        self.turn.enable()
        self.whiteScore.enable()
        self.blackScore.enable()
        self.move1.enable()
        self.move2.enable()
        self.move3.enable()
        self.move4.enable()
        self.move5.enable()
        self.helps.enable()