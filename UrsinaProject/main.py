from ursina import *


#SE DEFINE LA APP
tux_crusade = Ursina()

#[DEFINICIONES]
player = Entity(model='cube', color= color.red, position=Vec3(0, -3, 0), scale_y=1)

#[METODO GLOBAL]
#Se ejecuta en cada frame
def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

#[METODO GLOBAL]
#Escucha entradas del teclado o mouse
def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)

#SE EJECUTA LA APP
tux_crusade.run()