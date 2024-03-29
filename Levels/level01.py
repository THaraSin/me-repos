from ursina import *
from block import *

count = 0
normalSpeed = 3
boostSpeed  = 4
normalJump = 0.2

class Level01(Entity):
    def __init__(self):
        super().__init__()

        self.block_1_1 = NormalBlock((0, 1, 12))
        self.block_1_2 = NormalBlock((0, 2, 20))
        self.block_1_3 = JumpBlock((0, 2, 30))
        self.block_1_4 = NormalBlock((0, 12, 42))
        self.block_1_5 = NormalBlock((0, 12, 50))
        self.block_1_6 = SpeedBlock((0, 12, 62))
        self.block_1_7 = NormalBlock((0, 13, 74))
        
        self.finishBlock_1 = EndBlock(position = (0, 14, 88)) 
        self.ground_1 = StartBlock()

        self.player = None

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
        self.is_enabled = False

        self.block_1_1.disable()
        self.block_1_2.disable()
        self.block_1_3.disable()
        self.block_1_4.disable()
        self.block_1_5.disable()
        self.block_1_6.disable()
        self.block_1_7.disable()
        self.finishBlock_1.disable()
        self.ground_1.disable()

    def enable(self):
        self.is_enabled = True

        self.block_1_1.enable()
        self.block_1_2.enable()
        self.block_1_3.enable()
        self.block_1_4.enable()
        self.block_1_5.enable()
        self.block_1_6.enable()
        self.block_1_7.enable()
        self.finishBlock_1.enable()
        self.ground_1.enable()

    def update(self):
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_1.enabled == True:
            if hit.entity == self.ground_1:
                self.player.SPEED = normalSpeed
            if hit.entity == self.block_1_3:
                self.player.jump_height = 0.5
            elif hit.entity != self.block_1_3:
                self.player.jump_height = normalJump

            if hit.entity == self.block_1_6:
                self.player.SPEED = boostSpeed * 2.5
            
            if hit.entity == self.block_1_7:
                self.player.SPEED = normalSpeed
            
            if hit.entity == self.finishBlock_1:
                self.player.SPEED = normalSpeed
              