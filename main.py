from ursina import *
from block import *
from player import ThirdPersonController

from mainmenu import MainMenu
from pausemenu import PauseMenu

from Levels.level02 import Level02

application.development_mode = True

app = Ursina(borderless = False)

window.title = "This Game is Hella Lit!!! by THaraSin"
window.fps_counter.disable()

window.exit_button = False

sky = Sky(texture = "./assets/Sky")

light = PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

normalJump = 0.2
normalSpeed = 3

player = ThirdPersonController("cube", (0, 10, 0), "box", color = color.cyan)
player.jump_height = normalJump
player.SPEED = normalSpeed
player.disable()

level02 = Level02()
level02.player = player

m = MainMenu()
m.player = player
mouse.locked = False

def reset_player():
    player.position = (0, 3, 0)
    player.SPEED = normalSpeed
    player.jump_height = normalJump
    camera.rotation_z = 0

def input(key):
    if key == "escape":
        mouse.locked = False
        player.disable()
        
        p = PauseMenu()
        p.player = player

def update():
    if player.position.y <= -50:
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation_z = 0

    if held_keys["g"]:
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation_z = 0


app.run()