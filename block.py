from ursina import *

class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (3, 0.8, 3)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#C0C0C0",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation,
        )
        
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (3, 0.5, 8)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#385a7c",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (3, 0.8, 3)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#FF8B00",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class SuperBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (3, 0.8, 3)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#f97171",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class AbnorBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (3, 0.8, 3)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#7116FE",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class SlowBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (3, 0.5, 15)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#FFFF00",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class Wall(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = (5, 4, 1),
            color = "#964B00",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = (0, 0, 90)
        )

class BreakBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (3, 0.8, 3)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#800020 ",
            texture = "white_cube",
            position = position,
            rotaion = rotation
        )

class StartBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (10, 0.8, 10)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#CACACA",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class EndBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale_x = 10,
            scale_z = 10,
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )