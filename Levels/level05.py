from ursina import *
from block import *

count = 0
normalSpeed = 3
boostSpeed  = 4
normalJump = 0.2

class Level05(Entity):
    def __init__(self):
        super().__init__()

        self.block_5_1 = NormalBlock(position = (0, 1, 10))
        self.block_5_2 = AbnorBlock(position = (-3, 1, 18), rotation = (0, 0, 30))
        self.block_5_3 = NormalBlock(position = (3, 1, 26), rotation = (0, 0, -30))
        self.block_5_4 = AbnorBlock(position = (-3, 1, 34), rotation = (0, 0, 30))
        self.block_5_5 = NormalBlock(position = (3, 1, 42), rotation = (0, 0, -30))
        self.block_5_6 = AbnorBlock(position = (-3, 1, 50), rotation = (0, 0, 30))
        self.block_5_7 = NormalBlock(position = (3, 1, 58), rotation = (0, 0, -30))
        self.block_5_8 = AbnorBlock(position = (-3, 1, 66), rotation = (0, 0, 30))
        self.block_5_9 = SpeedBlock(position = (0, 1, 78))
        self.block_5_10 = NormalBlock(position = (0, 1, 95))

        self.ground_5 = StartBlock()
        self.finishBlock_5 = EndBlock(position = (0, 1, 105))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
        self.is_enabled = False

        self.block_5_1.disable()
        self.block_5_2.disable()
        self.block_5_3.disable()
        self.block_5_4.disable()
        self.block_5_5.disable()
        self.block_5_6.disable()
        self.block_5_7.disable()
        self.block_5_8.disable()
        self.block_5_9.disable()
        self.block_5_10.disable()
        self.finishBlock_5.disable()
        self.ground_5.disable()

    def enable(self):
        self.is_enabled = True

        self.block_5_1.enable()
        self.block_5_2.enable()
        self.block_5_3.enable()
        self.block_5_4.enable()
        self.block_5_5.enable()
        self.block_5_6.enable()
        self.block_5_7.enable()
        self.block_5_8.enable()
        self.block_5_9.enable()
        self.block_5_10.enable()
        self.finishBlock_5.enable()
        self.ground_5.enable()

    def update(self):
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_5.enabled == True:
            if hit.entity == self.block_5_2:
                camera.rotation_z = 180
            
            if hit.entity == self.block_5_3:
                camera.rotation_z = 0
            
            if hit.entity == self.block_5_4:
                camera.rotation_z = 180
            
            if hit.entity == self.block_5_5:
                camera.rotation_z = 0
            
            if hit.entity == self.block_5_6:
                camera.rotation_z = 180
            
            if hit.entity == self.block_5_7:
                camera.rotation_z = 0
            
            if hit.entity == self.block_5_8:
                camera.rotation_z = 180

            if hit.entity == self.block_5_9:
                camera.rotation_z = 0
                self.player.SPEED = boostSpeed * 2

            if hit.entity == self.block_5_10:
                self.player.SPEED = normalSpeed
        
            if hit.entity == self.finishBlock_5:
                camera.rotation_z = 0
                self.player.SPEED = normalSpeed