from ursina import *
import sys
from block import *

count = 0
normalSpeed = 3
boostSpeed  = 4
normalJump = 0.2

class Level02(Entity):
    def __init__(self):
        super().__init__()
        self.block_2_1 = NormalBlock((0, 1, 12))
        self.block_2_2 = NormalBlock((0, 2, 20))
        self.block_2_3 = NormalBlock((0, 3, 28))
        self.block_2_4 = NormalBlock((0, 4, 36))
        self.block_2_5 = NormalBlock((8, 5, 36))
        self.block_2_6 = NormalBlock((16, 6, 36))
        self.block_2_7 = JumpBlock((24, 2, 36))
        self.block_2_8 = NormalBlock((32, 10, 36))
        self.block_2_9 = SpeedBlock((32, 10, 46))

        self.ground_2 = StartBlock((0, -0.01, 0))
        self.finishBlock_2 = EndBlock((32, 10, 82))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
        self.is_enabled = False

        self.block_2_1.disable()
        self.block_2_2.disable()
        self.block_2_3.disable()
        self.block_2_4.disable()
        self.block_2_5.disable()
        self.block_2_6.disable()
        self.block_2_7.disable()
        self.block_2_8.disable()
        self.block_2_9.disable()
        self.finishBlock_2.disable()
        self.ground_2.disable()

    def enable(self):
        self.is_enabled = True

        self.block_2_1.enable()
        self.block_2_2.enable()
        self.block_2_3.enable()
        self.block_2_4.enable()
        self.block_2_5.enable()
        self.block_2_6.enable()
        self.block_2_7.enable()
        self.block_2_8.enable()
        self.block_2_9.enable()
        self.finishBlock_2.enable()
        self.ground_2.enable()

    def update(self):
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_2.enabled == True:
            if hit.entity == self.ground_2:
                self.player.SPEED = normalSpeed
            if hit.entity == self.block_2_7:
                self.player.jump_height = 0.4
            elif hit.entity != self.block_2_7:
                self.player.jump_height = normalJump

            if hit.entity == self.block_2_9:
                self.player.SPEED = boostSpeed * 2.5

            if hit.entity == self.finishBlock_2:
                global count
                self.player.SPEED = normalSpeed
                if count < 1:
                    Audio("./assets/Victory sound effect.wav", loop = False, volume = 3)
                    count += 1
                else:
                    pass
                pass
                
                
