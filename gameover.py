from ursina import *

class GameOver(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.gameover_menu = Entity(parent = self, enabled = True)
        self.player = None
        self.main_menu = None
        self.pause_menu = None

        self.level01 = None
        self.level02 = None
        self.level03 = None
        

        def retry():
            self.level01.enable()
            self.level02.disable()
            self.level03.disable()
            self.player.position = (0, 5, 0)
            self.player.enable()
            mouse.locked = True
            self.gameover_menu.disable()
    
        
        black = Entity(model = "quad", scale = (30, 30, 30), texture = "assets/black", parent = self.gameover_menu, y = 5)

        title = Entity(model = "quad", scale = (3, 0.25, 1), texture = "assets/youdied", parent = self.gameover_menu, y = 0.25)
        Audio("./assets/youdiedsound.wav", loop = False, volume = 0.1)

        
        retry_button = Button(text = "R e t r y", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, y = -0.16, parent = self.gameover_menu)
        quit_button = Button(text = "Q u i t", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, y = -0.3, parent = self.gameover_menu)
        quit_button.on_click = application.quit
        retry_button.on_click = Func(retry)