from ursina import *
from Levels.level04 import Level04
from block import *
from player import *

from Levels.level01 import Level01
from Levels.level02 import Level02
from Levels.level03 import Level03
from Levels.level04 import Level04
from Levels.level05 import Level05
from Levels.level06 import Level06
from Levels.level07 import Level07
from Levels.level08 import Level08
from Levels.level09 import Level09
from Levels.level10 import Level10

from mainmenu import *
from pausemenu import *
from finishmenu import *
from gameover import *

from Sky import *

application.development_mode = True
app = Ursina()

window.title = "This Game is Hella Lit!!! by THaraSin"
window.fps_counter.enable()
window.exit_button = False

#Sky
light = PointLight(parent = camera, position = (0, 10, -1.5), color = color.white)
AmbientLight(color = color.rgba(100, 100, 100, 0.1))
sky = Sky()

#Song
song = Song()
vic = Vic()
vic.stop()
die = Die()
die.stop()

#Player
c = 0
heart = 6
normalJump = 0.2
normalSpeed = 3
player = ThirdPersonController("cube", (0, 3, 0), "box", color = color.cyan)
player.jump_height = normalJump
player.SPEED = normalSpeed
player.disable()
mouse.locked = False

#Levels
level01 = Level01()
level01.player = player

level02 = Level02()
level02.player = player

level03 = Level03()
level03.player = player

level04 = Level04()
level04.player = player

level05 = Level05()
level05.player = player

level06 = Level06()
level06.player = player

level07 = Level07()
level07.player = player

level08 = Level08()
level08.player = player

level09 = Level09()
level09.player = player

level10 = Level10()
level10.player = player



#Mainmenu
m = MainMenu()
m.player = player
m.level01 = level01
m.level02 = level02
m.level03 = level03
m.level04 = level04
m.level05 = level05
m.level06 = level06
m.level07 = level07
m.level08 = level08
m.level09 = level09
m.level10 = level10
m.song = song
mouse.locked = False

level01.disable()
level02.disable() 
level03.disable() 
level04.disable() 
level05.disable() 
level06.disable()
level07.disable() 
level08.disable() 
level09.disable() 
level10.disable() 

#Heart
heart_1 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-1.15, 0.45, 0))
heart_2 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-1.09, 0.45, 0))
heart_3 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-1.03, 0.45, 0))
heart_4 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-0.97, 0.45, 0))
heart_5 = Entity(model = "quad", scale = 0.05, texture = "assets/heart", parent = camera.ui, position = (-0.91, 0.45, 0))

#Reset
def reset_player():
    player.position = (0, 3, 0)
    player.SPEED = normalSpeed
    player.jump_height = normalJump
    camera.rotation_z = 0

#Pausemenu
def input(key):
    if key == "escape":
        mouse.locked = False
        player.disable()
        
        p = PauseMenu()
        p.player = player
        p.level01 = level01
        p.level02 = level02
        p.level03 = level03
        p.level04 = level04
        p.level05 = level05
        p.level06 = level06
        p.level07 = level07
        p.level08 = level08
        p.level09 = level09 
        p.level10 = level10
        p.song = song

#Update
def update():
    global count, heart, c, lev

    if player.position.y <= -50:
            player.position = Vec3(0, 5, 0)
            player.SPEED = normalSpeed
            player.jump_height = normalJump
            camera.rotation = (10, 0, 0)
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
            g = GameOver()
            g.player = player
            g.level01 = level01
            g.level02 = level02
            g.level03 = level03
            g.level04 = level04
            g.level05 = level05
            g.level06 = level06
            g.level07 = level07
            g.level08 = level08
            g.level09 = level09
            g.level10 = level10
            g.song = song
            g.die = die
            song.stop()
            die.play()
            level01.enable()
            level02.disable()
            level03.disable()
            level04.disable()
            level05.disable()
            level06.disable()
            level07.disable()
            level08.disable()
            level09.disable()
            level10.disable()
            heart_5.visible = True
            heart_4.visible = True
            heart_3.visible = True
            heart_2.visible = True
            heart_1.visible = True
            heart += 6
            c -= 1
        
    hit = raycast(player.position, player.down, distance = 2, ignore = [player, ])

    if hit.entity == level01.finishBlock_1:
        player.disable()
        level01.disable()
        level02.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        song.stop()
        f.vic = vic
        vic.play()
             
    if hit.entity == level02.finishBlock_2:
        player.disable()
        level02.disable()
        level03.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04 
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song  
        song.stop() 
        f.vic = vic
        vic.play()  

    if hit.entity == level03.finishBlock_3:
        player.disable()
        level03.disable()
        level04.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        camera.rotation_z = 0
        camera.rotation_y = 0
        song.stop()
        f.vic = vic
        vic.play()
    
    if hit.entity == level04.finishBlock_4:
        player.disable()
        level04.disable()
        level05.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04 
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        song.stop()
        f.vic = vic
        vic.play()

    if hit.entity == level05.finishBlock_5:
        player.disable()
        level05.disable()
        level06.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04 
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        song.stop()
        f.vic = vic
        vic.play()
    
    if hit.entity == level06.finishBlock_6:
        player.disable()
        level06.disable()
        level07.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04 
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        song.stop()
        f.vic = vic
        vic.play()
    
    if hit.entity == level07.finishBlock_7:
        player.disable()
        level07.disable()
        level08.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04 
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        song.stop()
        f.vic = vic
        vic.play()
    
    if hit.entity == level08.finishBlock_8:
        player.disable()
        level08.disable()
        level09.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04 
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        song.stop()
        f.vic = vic
        vic.play()
    
    if hit.entity == level09.finishBlock_9:
        player.disable()
        level09.disable()
        level10.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04 
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        song.stop()
        f.vic = vic
        vic.play()
    
    if hit.entity == level10.finishBlock_10:
        player.disable()
        level10.disable()
        level01.enable()
        mouse.locked = False
        f = FinishMenu()
        f.player = player
        f.level01 = level01
        f.level02 = level02
        f.level03 = level03
        f.level04 = level04 
        f.level05 = level05
        f.level06 = level06
        f.level07 = level07
        f.level08 = level08
        f.level09 = level09 
        f.level10 = level10
        f.song = song
        song.stop()
        f.vic = vic
        vic.play()
            
app.run()

