from ursina import *
from block import *

count = 0
normalSpeed = 3
boostSpeed  = 4
normalJump = 0.2


class Level03(Entity):
    def __init__(self):
        super().__init__()

        self.block_3_1 = NormalBlock(position = (0, 1, 10))
        self.block_3_2 = NormalBlock(position = (0, 2, 18))
        self.block_3_3 = NormalBlock(position = (8, 3, 18))
        self.block_3_4 = NormalBlock(position = (16, 4, 18))
        self.block_3_5 = NormalBlock(position = (16, 5, 10))
        self.block_3_6 = NormalBlock(position = (16, 6, 2))
        self.block_3_7 = NormalBlock(position = (8, 7, 2))
        self.block_3_8 = NormalBlock(position = (8, 8, 10))
        self.block_3_9 = NormalBlock(position = (8, 9, 18))
        self.block_3_10 = NormalBlock(position = (16, 10, 18))
        self.block_3_11 = NormalBlock(position = (16, 11, 10))
        self.block_3_12 = NormalBlock(position = (16, 12, 2))
        self.block_3_13 = NormalBlock(position = (8, 13, 2))
        self.block_3_14 = NormalBlock(position = (8, 14, -6))
        self.block_3_15 = JumpBlock(position = (8, 15, -15))
        self.block_3_16 = JumpBlock(position = (8, 38, -25))
        self.block_3_17 = JumpBlock(position = (8, 61, -15))

        self.finishBlock_3 = EndBlock(position = (8, 84, -25))
        self.ground_3 = StartBlock()

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
        self.is_enabled = False

        self.block_3_1.disable()
        self.block_3_2.disable()
        self.block_3_3.disable()
        self.block_3_4.disable()
        self.block_3_5.disable()
        self.block_3_6.disable()
        self.block_3_7.disable()
        self.block_3_8.disable()
        self.block_3_9.disable()
        self.block_3_10.disable()
        self.block_3_11.disable()
        self.block_3_12.disable()
        self.block_3_13.disable()
        self.block_3_14.disable()
        self.block_3_15.disable()
        self.block_3_16.disable()
        self.block_3_17.disable()
        self.finishBlock_3.disable()
        self.ground_3.disable()

    def enable(self):
        self.is_enabled = True

        self.block_3_1.enable()
        self.block_3_2.enable()
        self.block_3_3.enable()
        self.block_3_4.enable()
        self.block_3_5.enable()
        self.block_3_6.enable()
        self.block_3_7.enable()
        self.block_3_8.enable()
        self.block_3_9.enable()
        self.block_3_10.enable()
        self.block_3_11.enable()
        self.block_3_12.enable()
        self.block_3_13.enable()
        self.block_3_14.enable()
        self.block_3_15.enable()
        self.block_3_16.enable()
        self.block_3_17.enable()
        self.finishBlock_3.enable()
        self.ground_3.enable()   
    
    def update(self):
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_3.enabled == True:
            if hit.entity == self.ground_3:
                self.player.SPEED = normalSpeed
            if hit.entity == self.block_3_15:
                self.player.jump_height = 0.5
            if hit.entity == self.block_3_16:
                self.player.jump_height = 0.5
        
        if hit.entity == self.finishBlock_3:
                self.player.SPEED = normalSpeed
               