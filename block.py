from ursina import *

class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#C0C0C0",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation,
        )
        
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0), scale = (3, 0.5, 8)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#9370DB",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#FF8B00",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class Wall(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = (5, 4, 1),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = (0, 0, 90)
        )

class MovingBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#2D49FB",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class StartBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale_x = 10,
            scale_z = 10,
            color = "#CACACA",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

class EndBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale_x = 10,
            scale_z = 10,
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
        )