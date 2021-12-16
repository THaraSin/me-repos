from ursina import *
from Sky import *

class GameOver(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.gameover_menu = Entity(parent = self, enabled = True)
        self.levels_menu = Entity(parent = self, enabled = False)
        self.player = None
        self.main_menu = None
        self.pause_menu = None

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
        self.die = None

        def retry():
            self.player.position = (0, 5, 0)
            self.player.enable()
            mouse.locked = True
            self.gameover_menu.disable()
            self.song.play()
            self.die.stop()
        
        def levelselect(): 
            self.gameover_menu.disable() 
            self.levels_menu.enable() 
        
        def level01(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.enable() 
            self.level02.disable() 
            self.level03.disable()
            self.level04.disable()
            self.level05.disable() 

            self.song.play()
            self.die.stop()
            
        def level02(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable() 
            self.level02.enable() 
            self.level03.disable()
            self.level04.disable()
            self.level05.disable() 

            self.song.play()
            self.die.stop()
            
        def level03(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable()  
            self.level03.enable() 
            self.level04.disable()
            self.level05.disable() 

            self.song.play()
            self.die.stop()
        
        def level04(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable() 
            self.level03.disable() 
            self.level04.enable() 
            self.level05.disable() 

            self.song.play()
            self.die.stop()
        
        def level05(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable() 
            self.level03.disable() 
            self.level04.disable() 
            self.level05.enable() 

            self.song.play()
            self.die.stop()
        
        def level06(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable() 
            self.level03.disable() 
            self.level04.disable() 
            self.level05.disable()
            self.level06.enable() 
            self.level07.disable() 
            self.level08.disable()
            self.level09.disable()
            self.level10.disable()

            self.song.play()
            self.die.stop()
        
        def level07(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable() 
            self.level02.disable() 
            self.level03.disable()
            self.level04.disable()
            self.level05.disable()
            self.level06.disable() 
            self.level07.enable() 
            self.level08.disable()
            self.level09.disable()
            self.level10.disable()

            self.song.play()
            self.die.stop()
            
        def level08(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable() 
            self.level02.disable() 
            self.level03.disable()
            self.level04.disable()
            self.level05.disable()
            self.level06.disable() 
            self.level07.disable() 
            self.level08.enable()
            self.level09.disable()
            self.level10.disable()

            self.song.play()
            self.die.stop()
            
        def level09(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable()  
            self.level03.disable() 
            self.level04.disable()
            self.level05.disable()
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable()
            self.level09.enable()
            self.level10.disable()

            self.song.play()
            self.die.stop()
        
        def level10(): 
            self.gameover_menu.disable() 
            self.levels_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable() 
            self.level03.disable() 
            self.level04.disable()
            self.level05.disable()
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable()
            self.level09.disable()
            self.level10.enable()

            self.song.play()
            self.die.stop()

        def back():
            self.gameover_menu.enable()
            self.levels_menu.disable()
    
        
        black = Entity(model = "quad", scale = (30, 30, 30), texture = "assets/black", parent = self.gameover_menu, y = 5)
        black = Entity(model = "quad", scale = (30, 30, 30), texture = "assets/black", parent = self.levels_menu, y = 5)
        title = Entity(model = "quad", scale = (3, 0.25, 1), texture = "assets/youdied", parent = self.gameover_menu, y = 0.25)

        retry_button = Button(text = "R e t r y", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, y = -0.05, parent = self.gameover_menu)
        levelselect_button = Button(text = "L e v e l - S e l e c t", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, y = -0.2, parent = self.gameover_menu)
        quit_button = Button(text = "Q u i t", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, y = -0.35, parent = self.gameover_menu)
        quit_button.on_click = application.quit
        levelselect_button.on_click = Func(levelselect)
        retry_button.on_click = Func(retry)

        level01_button = Button(text = "L e v e l 0 1", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = 0.3, parent = self.levels_menu) 
        level02_button = Button(text = "L e v e l 0 2", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = 0.1, parent = self.levels_menu) 
        level03_button = Button(text = "L e v e l 0 3", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = -0.1, parent = self.levels_menu)

        level04_button = Button(text = "L e v e l 0 4", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = 0, y = 0.3, parent = self.levels_menu) 
        level05_button = Button(text = "L e v e l 0 5", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = 0, y = 0.1, parent = self.levels_menu)  
        level06_button = Button(text = "L e v e l 0 6", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = 0, y = -0.1, parent = self.levels_menu)

        level07_button = Button(text = "L e v e l 0 7", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = 0.3, parent = self.levels_menu)
        level08_button = Button(text = "L e v e l 0 8", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = 0.1, parent = self.levels_menu)  
        level09_button = Button(text = "L e v e l 0 9", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = -0.1, parent = self.levels_menu)

        level10_button = Button(text = "L e v e l 1 0", color = color.black, text_color = color.red, scale_y = 0.1, scale_x = 0.3, x = 0, y = -0.3, parent = self.levels_menu)
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