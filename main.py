from ursina import *
from block import *
from player import ThirdPersonController

from mainmenu import MainMenu
from pausemenu import PauseMenu

from Levels.level01 import Level01
from Levels.level02 import Level02

application.development_mode = True

app = Ursina()

window.title = "This Game is Hella Lit!!! by THaraSin"
window.fps_counter.enable()
window.exit_button = False

sky = Sky(texture = "./assets/Sky")

light = PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

count = 0
normalJump = 0.2
normalSpeed = 3

player = ThirdPersonController("cube", (0, 3, 0), "box", color = color.cyan, texture = "sky_sunset")
player.jump_height = normalJump
player.SPEED = normalSpeed
player.disable()

level01 = Level01()
level01.player = player

level02 = Level02()
level02.player = player

m = MainMenu()
m.player = player
mouse.locked = False

class FinishMenu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.finish_menu = Entity(parent = self, enabled = True)
        self.player = None
        self.main_menu = None

        def reset():
            self.player.position = (0, 5, 0)
            self.player.enable()
            mouse.locked = True
            self.finish_menu.disable()

        def next_level():
            if Level01.enable:
                level01.disable()
                level02.enable()
            self.player.position = (0, 5, 0)
            self.player.enable()
            mouse.locked = True
            self.finish_menu.disable()

        nextlevel_button = Button(text = "Next Level", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.12, parent = self.finish_menu)
        reset_button = Button(text = "R e s e t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0, parent = self.finish_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.12, parent = self.finish_menu)
        quit_button.on_click = application.quit
        reset_button.on_click = Func(reset)
        nextlevel_button.on_click = Func(next_level)

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
        p.level01 = level01
        p.level02 = level02

def update():
    global count
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

    hit = raycast(player.position, player.down, distance = 2, ignore = [player, ])
    
    
    if hit.entity == level01.finishBlock_1:
        if count <1:
            player.disable()
            Level01.disable
            mouse.locked = False
            f = FinishMenu()
            f.player = player
            count += 1
        else:
            pass
        

app.run()