from ursina import *

app = Ursina()

penguinTower = 'Tower Penguin.obj'
tower = 'Tower 01.obj'

player = Entity(model=penguinTower, color=color.blue, position=Vec3(0, -3, 0), scale_y=1)
fichaUno = Entity(model=tower, color=color.red, position=Vec3(-1, 1, 0))
fichaDos = Entity(model=tower, color=color.green, position=Vec3(-2, 2, 0))
fichaTres = Entity(model=tower, color=color.pink, position=Vec3(1, -1, 0))
fichaCuatro = Entity(model=tower, color=color.yellow, position=Vec3(2, -2, 0))

def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)

app.run()