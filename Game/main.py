from ursina import *
from ground import *
from player import Player

app = Ursina()

light = Pointlight(parent = camera, position = (0, 0, -1.5))
light.color = "#F3E7D3"

AmbientLight(color = (100, 100, 100, 0.1))

Sky()

normalJump = 0.3
normalSpeed = 1.5 

player = Player("cube, ("0, 10, 0), "box", controls ="wasd")
player.jump.hight. normalJump
player.SPEED = normalspeed


app.run()