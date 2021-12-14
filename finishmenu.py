from ursina import *

count = 0

class FinishMenu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.finish_menu = Entity(parent = self, enabled = True)
        self.player = None
        self.main_menu = None
        self.pause_menu = None

        def reset():
            self.player.position = (0, 5, 0)
            self.player.enable()
            mouse.locked = True
            self.finish_menu.disable()

        def next_level():
            global count
            self.player.position = (0, 5, 0)
            self.finish_menu.disable()
            self.player.enable()
            mouse.locked = True
            count == 0
        
        title = Entity(model = "quad", scale = (1, 0.3, 1), texture = "assets/royale", parent = self.finish_menu, y = 0.25)

        nextlevel_button = Button(text = "Next Level", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.02, parent = self.finish_menu)
        reset_button = Button(text = "R e s e t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.16, parent = self.finish_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.3, parent = self.finish_menu)
        quit_button.on_click = application.quit
        reset_button.on_click = Func(reset)
        nextlevel_button.on_click = Func(next_level)