from ursina import *
from block import *

count = 0
normalSpeed = 3
boostSpeed  = 4
normalJump = 0.2

class Level08(Entity):
    def __init__(self):
        super().__init__()

        self.block_8_1 = NormalBlock(position = (0, 0, 13))
        self.block_8_2 = NormalBlock(position = (0, -20, 19))
        self.block_8_3 = SlowBlock(position = (0, -20, 31))
        self.block_8_4 = NormalBlock(position = (0, -20, 43))
        self.block_8_5 = NormalBlock(position = (0, -20, 50))
        self.block_8_6 = NormalBlock(position = (0, -20, 57))
        self.block_8_7 = NormalBlock(position = (0, -20, 64))
        self.block_8_8 = NormalBlock(position = (0, -22, 72))
        self.block_8_9 = NormalBlock(position = (0, -24, 80))
        self.block_8_10 = NormalBlock(position = (0, -26, 88))
        self.block_8_11 = SuperBlock(position = (0, -26, 95))

        self.ground_8 = StartBlock()
        self.finishBlock_8 = EndBlock(position = (0, -10, 350))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
        self.is_enabled = False

        self.block_8_1.disable()
        self.block_8_2.disable()
        self.block_8_3.disable()
        self.block_8_4.disable()
        self.block_8_5.disable()
        self.block_8_6.disable()
        self.block_8_7.disable()
        self.block_8_8.disable()
        self.block_8_9.disable()
        self.block_8_10.disable()
        self.block_8_11.disable()
        self.finishBlock_8.disable()
        self.ground_8.disable()

    def enable(self):
        self.is_enabled = True

        self.block_8_1.enable()
        self.block_8_2.enable()
        self.block_8_3.enable()
        self.block_8_4.enable()
        self.block_8_5.enable()
        self.block_8_6.enable()
        self.block_8_7.enable()
        self.block_8_8.enable()
        self.block_8_9.enable()
        self.block_8_10.enable()
        self.block_8_11.enable()
        self.finishBlock_8.enable()
        self.ground_8.enable()

    def update(self):
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_8.enabled == True:
            if hit.entity == self.block_8_3:
                self.player.SPEED = 1
                
            if hit.entity == self.block_8_11:
                self.player.SPEED = boostSpeed * 5.5
                self.player.jump_height = 1.4

            if hit.entity == self.finishBlock_8:
                camera.rotation_z = 0
                self.player.SPEED = normalSpeed