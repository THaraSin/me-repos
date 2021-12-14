from ursina import *
from block import *
from player import ThirdPersonController

from Levels.level01 import Level01
from Levels.level02 import Level02
from Levels.level03 import Level03

from mainmenu import *
from pausemenu import *
from finishmenu import *
from gameover import *



application.development_mode = True

app = Ursina()

window.title = "This Game is Hella Lit!!! by THaraSin"
window.fps_counter.enable()
window.exit_button = False

song = Audio("./assets/ghostrunner.wav", loop = True, volume = 0.5)

sky = Sky(texture = "./assets/Sky")

light = PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))


#Player
c = 0
oof = 0
heart = 6
normalJump = 0.2
normalSpeed = 3
player = ThirdPersonController("cube", (0, 3, 0), "box", color = color.cyan)
player.jump_height = normalJump
player.SPEED = normalSpeed
player.disable()

mouse.locked = False

level01 = Level01()
level01.player = player

level02 = Level02()
level02.player = player

level03 = Level03()
level03.player = player

m = MainMenu()
m.player = player
m.level01 = level01
m.level02 = level02
m.level03 = level03

mouse.locked = False

heart_1 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-1.15, 0.45, 0))
heart_2 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-1.09, 0.45, 0))
heart_3 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-1.03, 0.45, 0))
heart_4 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-0.97, 0.45, 0))
heart_5 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-0.91, 0.45, 0))
   
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
        p.level03 = level03

def update():
    global count, heart, c, oof, g

    if player.position.y <= -50:
            player.position = Vec3(0, 5, 0)
            player.SPEED = normalSpeed
            player.jump_height = normalJump
            camera.rotation = (0, 0, 0)
            Audio("./assets/Oof.wav", loop = False, volume = 0.5)
            heart -= 1

    if heart == 5:
        heart_5.visible = False       
    if heart == 4:
        heart_4.visible = False
    if heart == 3:
        heart_3.visible = False
    if heart == 2:
        heart_2.visible = False
    if heart == 1:
        heart_1.visible = False
    
    if heart == 0:
        if c < 1:
            Audio("./assets/Oof.wav", loop = False, volume = 0.5)
            player.disable()
            mouse.locked = False
            c += 1
            song.stop()
            g = GameOver()
            g.player = player
            g.level01 = level01
            g.level02 = level02
            g.level03 = level03
            level01.disable()
            level02.disable()
            level03.disable()
            heart_5.visible = True
            heart_4.visible = True
            heart_3.visible = True
            heart_2.visible = True
            heart_1.visible = True
            heart += 6
            c -= 1
            oof == 0
        
    hit = raycast(player.position, player.down, distance = 2, ignore = [player, ])
    
    if hit.entity == level01.finishBlock_1:
        player.disable()
        level02.enable()
        level01.disable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player

    if hit.entity == level02.finishBlock_2: 
        player.disable()
        level01.disable()
        level02.disable()
        level03.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player         

    if hit.entity == level03.finishBlock_3:
        player.disable()
        level03.disable()
        level01.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
            
app.run()

