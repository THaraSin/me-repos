from ursina import *
from block import *

count = 0
normalSpeed = 3
boostSpeed  = 4
normalJump = 0.2


class Level04(Entity):
    def __init__(self):
        super().__init__()

        self.block_4_1 = NormalBlock(position = (0, 1, 12))
        self.block_4_2 = NormalBlock(position = (0, 2, 20))
        self.block_4_3 = JumpBlock(position = (0, -49, 40), scale = (8, 0.8, 8))
        self.block_4_4 = SpeedBlock(position = (0, 50, 93), scale = (3, 0.5, 50))
        self.block_4_5 = JumpBlock(position = (0, 15, 163), scale = (8, 0.8, 8))

        self.ground_4 = StartBlock()
        self.finishBlock_4 = EndBlock(position = (0, 20, 240))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
        self.is_enabled = False

        self.block_4_1.disable()
        self.block_4_2.disable()
        self.block_4_3.disable()
        self.block_4_4.disable()
        self.block_4_5.disable()
        self.finishBlock_4.disable()
        self.ground_4.disable()

    def enable(self):
        self.is_enabled = True

        self.block_4_1.enable()
        self.block_4_2.enable()
        self.block_4_3.enable()
        self.block_4_4.enable()
        self.block_4_5.enable()
        self.finishBlock_4.enable()
        self.ground_4.enable()

    def update(self):
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_4.enabled == True:
            if hit.entity == self.block_4_3:
                self.player.jump_height = 1.1
            elif hit.entity != self.block_4_3:
                self.player.jump_height = normalJump

            if hit.entity == self.block_4_4:
                self.player.SPEED = boostSpeed * 2

            if hit.entity == self.block_4_5:
                self.player.SPEED = normalSpeed
                self.player.jump_height = 2

            if hit.entity == self.finishBlock_4:
                self.player.SPEED = normalSpeed
        