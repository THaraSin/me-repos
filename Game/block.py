from ursina import *

class NormalBlok(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            collider = "box",
            scale = (3, 0,8, 3),
            color = "#F26A1B",
            texture = "white_cube"
        )