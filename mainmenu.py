from ursina import *
from Sky import *

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
        self.level04 = None
        self.level05 = None
        self.level06 = None
        self.level07 = None
        self.level08 = None
        self.level09 = None
        self.level10 = None

        self.song = None
        
        def start():
            self.player.enable()
            mouse.locked = True 
            self.main_menu.disable() 

            self.level01.enable() 
            
        def levelselect(): 
            self.main_menu.disable() 
            self.levels_menu.enable() 
        
        def level01(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 

            self.level04.disable()
            self.level01.enable() 
            
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
        
        def level04(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 

            self.level01.disable() 
            self.level04.enable() 

        def level05(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level05.enable()

        def level06(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 

            self.level01.disable()
            self.level06.enable() 
            
        def level07(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 

            self.level01.disable() 
            self.level07.enable() 
            
        def level08(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 

            self.level01.disable() 
            self.level08.enable() 
        
        def level09(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            mouse.locked = True 

            self.level01.disable() 
            self.level09.enable() 

        def level10(): 
            self.main_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level10.enable() 

        def back():
            self.main_menu.enable()
            self.levels_menu.disable()
            
        title = Entity(model = "quad", scale = (1, 1, 1), texture = "assets/hella lit", parent = self.main_menu, scale_x = 1.2, y = 0.25) 

        start_button = Button(text = "S t a r t - G a m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.07, parent = self.main_menu) 
        levelselect_button = Button(text = "L e v e l - S e l e c t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.21, parent = self.main_menu) 
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.35, parent = self.main_menu) 
        start_button.on_click = Func(start) 
        levelselect_button.on_click = Func(levelselect)
        quit_button.on_click = application.quit 
        
        level01_button = Button(text = "L e v e l 0 1", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = 0.3, parent = self.levels_menu) 
        level02_button = Button(text = "L e v e l 0 2", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = 0.1, parent = self.levels_menu) 
        level03_button = Button(text = "L e v e l 0 3", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = -0.1, parent = self.levels_menu)
  
        level04_button = Button(text = "L e v e l 0 4", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = 0.3, parent = self.levels_menu) 
        level05_button = Button(text = "L e v e l 0 5", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = 0.1, parent = self.levels_menu)
        level06_button = Button(text = "L e v e l 0 6", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = -0.1, parent = self.levels_menu)

        level07_button = Button(text = "L e v e l 0 7", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = 0.3, parent = self.levels_menu)
        level08_button = Button(text = "L e v e l 0 8", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = 0.1, parent = self.levels_menu)  
        level09_button = Button(text = "L e v e l 0 9", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = -0.1, parent = self.levels_menu)
        
        level10_button = Button(text = "L e v e l 1 0", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = -0.3, parent = self.levels_menu)
        back_button = Button(text = "< - B a c k", color = color.gray, scale_y = 0.05, scale_x = 0.2, y = -0.4, parent = self.levels_menu)

        level01_button.on_click = Func(level01) 
        level02_button.on_click = Func(level02) 
        level03_button.on_click = Func(level03)

        level04_button.on_click = Func(level04)
        level05_button.on_click = Func(level05)
        level06_button.on_click = Func(level06)

        level07_button.on_click = Func(level07) 
        level08_button.on_click = Func(level08) 
        level09_button.on_click = Func(level09)

        level10_button.on_click = Func(level10)

        back_button.on_click = Func(back)
