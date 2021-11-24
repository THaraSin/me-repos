from ursina import *
from block import *
from player import Player

app = Ursina()

PointLight(parent = camera, position = (0, 0, -1.5), color = "#F3E7D3")
AmbientLight(color = (100, 100, 100, 0.1))

sky = Sky(texture = "./assets/Sky")

normalJump = 0.3
normalSpeed = 1.5 

player = Player("cube", (0, 10, 0), "box", controls ="wasd")
player.jump.hight. normalJump
player.SPEED = normalSpeed


app.run()