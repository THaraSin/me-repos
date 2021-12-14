from ursina import *

class MainMenu(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

        self.main_menu = Entity(parent = self, enabled = True)
        self.levels_menu = Entity(parent = self, enabled = False)
        self.player = None

        self.level01 = None
        self.level02 = None
        self.level03 = None

        song = Audio("./assets/ghostrunner", loop = True, volume = 1)
        song.play()
        
        def start():
            self.player.enable()
            mouse.locked = True 
            self.main_menu.disable() 
            
        def levelselect(): 
            self.main_menu.disable() 
            self.levels_menu.enable() 
        
        def level01(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 
            
        def level02(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 

            self.level01.disable() 
            self.level02.enable() 
            
        def level03(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 

            self.level01.disable() 
            self.level03.enable() 

        def back():
            self.main_menu.enable()
            self.levels_menu.disable()
            
        title = Entity(model = "quad", scale = (1, 1, 1), texture = "assets/hella lit", parent = self.main_menu, y = 0.3) 

        start_button = Button(text = "S t a r t - G a m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.02, parent = self.main_menu) 
        levelselect_button = Button(text = "L e v e l - S e l e c t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.16, parent = self.main_menu) 
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.3, parent = self.main_menu) 
        start_button.on_click = Func(start) 
        levelselect_button.on_click = Func(levelselect)
        quit_button.on_click = application.quit 
        
        level01_button = Button(text = "L e v e l 0 1", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.2, parent = self.levels_menu) 
        level02_button = Button(text = "L e v e l 0 2", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0, parent = self.levels_menu) 
        level03_button = Button(text = "L e v e l 0 3", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.2, parent = self.levels_menu) 
        
        back_button = Button(text = "< - B a c k", color = color.gray, scale_y = 0.05, scale_x = 0.2, y = -0.4, parent = self.levels_menu)

        level01_button.on_click = Func(level01) 
        level02_button.on_click = Func(level02) 
        level03_button.on_click = Func(level03)

        back_button.on_click = Func(back)
