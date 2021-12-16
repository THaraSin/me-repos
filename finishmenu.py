from ursina import *
from Sky import *

count = 0
lev = 0

class FinishMenu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.finish_menu = Entity(parent = self, enabled = True)
        self.levels_main_menu = Entity(parent = self, enabled = False)
        self.levels_fin_menu = Entity(parent = self, enabled = False)
        self.main_menu = Entity(parent = self, enabled = False)
        self.player = None
        self.pause_menu = None

        self.level01 = None
        self.level02 = None
        self.level03 = None
        self.level05 = None
        self.level06 = None
        self.level07 = None
        self.level08 = None
        self.level09 = None
        self.level10 = None
        self.level05 = None
        self.level06 = None
        self.level07 = None
        self.level08 = None
        self.level09 = None
        self.level10 = None

        self.song = None
        self.vic = None

        def next_level():
            global count
            self.player.position = (0, 5, 0)
            self.finish_menu.disable()
            self.player.enable()
            mouse.locked = True
            count == 0
            self.song.play()
            self.vic.stop()
        
        def start():
            self.player.enable()
            mouse.locked = True 
            self.main_menu.disable() 
            self.finish_menu.disable()
            self.player.position = (0, 5, 0)

            self.level01.enable() 
            self.level02.disable() 
            self.level03.disable() 
            self.level04.disable() 
            self.level05.disable() 
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable() 
            self.level09.disable() 
            self.level10.disable() 

            self.song.play()
        
        def mainmenu():
            self.main_menu.enable() 
            self.levels_fin_menu.disable() 
            self.levels_main_menu.disable() 
            self.finish_menu.disable()

            self.level01.disable() 
            self.level02.disable() 
            self.level03.disable() 
            self.level04.disable() 
            self.level05.disable() 
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable() 
            self.level09.disable() 
            self.level10.disable()  

            self.vic.stop()
            self.song.play()

        def levelselect_main(): 
            self.main_menu.disable() 
            self.levels_main_menu.enable() 
            self.levels_fin_menu.disable() 
        
        def levelselect_fin(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.enable() 
        
        def level01(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable() 
            self.main_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.enable() 
            self.level02.disable() 
            self.level03.disable()
            self.level04.disable()
            self.level05.disable()
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable()
            self.level09.disable()
            self.level10.disable()

            self.song.play()
            self.vic.stop()
            
        def level02(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable()  
            self.main_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable() 
            self.level02.enable() 
            self.level03.disable()
            self.level04.disable()
            self.level05.disable()
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable()
            self.level09.disable()
            self.level10.disable()

            self.song.play()
            self.vic.stop()
            
        def level03(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable()  
            self.main_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable()  
            self.level03.enable() 
            self.level04.disable()
            self.level05.disable()
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable()
            self.level09.disable()
            self.level10.disable()

            self.song.play()
            self.vic.stop()
        
        def level04(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable()  
            self.main_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable() 
            self.level03.disable() 
            self.level04.enable()
            self.level05.disable()
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable()
            self.level09.disable()
            self.level10.disable()

            self.song.play()
            self.vic.stop()
        
        def level05(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable()  
            self.main_menu.disable() 
            self.player.enable() 
            self.player.position = (0, 5, 0)
            mouse.locked = True 

            self.level01.disable()
            self.level02.disable() 
            self.level03.disable() 
            self.level04.disable() 
            self.level05.enable()
            self.level06.disable() 
            self.level07.disable() 
            self.level08.disable()
            self.level09.disable()
            self.level10.disable()

            self.song.play()
            self.vic.stop()
        
        def level06(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable()  
            self.main_menu.disable() 
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
            self.vic.stop()
        
        def level07(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable()  
            self.main_menu.disable() 
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
            self.vic.stop()
            
        def level08(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable()  
            self.main_menu.disable() 
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
            self.vic.stop()
            
        def level09(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable() 
            self.main_menu.disable()  
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
            self.vic.stop()
        
        def level10(): 
            self.finish_menu.disable() 
            self.levels_main_menu.disable() 
            self.levels_fin_menu.disable()  
            self.main_menu.disable() 
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
            self.vic.stop()

        def back_fin():
            self.finish_menu.enable()
            self.levels_fin_menu.disable()
            
        def back_main():
            self.main_menu.enable() 
            self.levels_main_menu.disable() 
            self.finish_menu.disable()
        
        title_1 = Entity(model = "quad", scale = (1, 0.3, 1), texture = "assets/royale", parent = self.finish_menu, y = 0.3)
        title_2 = Entity(model = "quad", scale = (1, 1, 1), texture = "assets/hella lit", parent = self.main_menu, scale_x = 1.2, y = 0.25) 

        nextlevel_button = Button(text = "Next Level", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.05, parent = self.finish_menu)
        levelselect_fin_button = Button(text = "L e v e l - S e l e c t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.finish_menu) 
        mainmenu_button = Button(text = "M a i n - M e n u", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.25, parent = self.finish_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.4, parent = self.finish_menu)
        quit_button.on_click = application.quit
        levelselect_fin_button.on_click = Func(levelselect_fin)
        nextlevel_button.on_click = Func(next_level)
        mainmenu_button.on_click = Func(mainmenu)

        start_button = Button(text = "S t a r t - G a m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.07, parent = self.main_menu) 
        levelselect_main_button = Button(text = "L e v e l - S e l e c t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.21, parent = self.main_menu) 
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.35, parent = self.main_menu)  
        start_button.on_click = Func(start) 
        levelselect_main_button.on_click = Func(levelselect_main)
        quit_button.on_click = application.quit 

        level01_button = Button(text = "L e v e l 0 1", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = 0.3, parent = self.levels_main_menu) 
        level02_button = Button(text = "L e v e l 0 2", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = 0.1, parent = self.levels_main_menu) 
        level03_button = Button(text = "L e v e l 0 3", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = -0.1, parent = self.levels_main_menu)

        level04_button = Button(text = "L e v e l 0 4", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = 0.3, parent = self.levels_main_menu)
        level05_button = Button(text = "L e v e l 0 5", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = 0.1, parent = self.levels_main_menu)  
        level06_button = Button(text = "L e v e l 0 6", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = -0.1, parent = self.levels_main_menu)

        level07_button = Button(text = "L e v e l 0 7", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = 0.3, parent = self.levels_main_menu)
        level08_button = Button(text = "L e v e l 0 8", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = 0.1, parent = self.levels_main_menu)  
        level09_button = Button(text = "L e v e l 0 9", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = -0.1, parent = self.levels_main_menu)

        level10_button = Button(text = "L e v e l 1 0", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = -0.3, parent = self.levels_main_menu)
        back_main_button = Button(text = "< - B a c k", color = color.gray, scale_y = 0.05, scale_x = 0.2, y = -0.4, parent = self.levels_main_menu)

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
        back_main_button.on_click = Func(back_main)

        level01_button = Button(text = "L e v e l 0 1", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = 0.3, parent = self.levels_fin_menu) 
        level02_button = Button(text = "L e v e l 0 2", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = 0.1, parent = self.levels_fin_menu) 
        level03_button = Button(text = "L e v e l 0 3", color = color.black, scale_y = 0.1, scale_x = 0.3, x = -0.4, y = -0.1, parent = self.levels_fin_menu)

        level04_button = Button(text = "L e v e l 0 4", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = 0.3, parent = self.levels_fin_menu)
        level05_button = Button(text = "L e v e l 0 5", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = 0.1, parent = self.levels_fin_menu)  
        level06_button = Button(text = "L e v e l 0 6", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = -0.1, parent = self.levels_fin_menu)

        level07_button = Button(text = "L e v e l 0 7", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = 0.3, parent = self.levels_fin_menu)
        level08_button = Button(text = "L e v e l 0 8", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = 0.1, parent = self.levels_fin_menu)  
        level09_button = Button(text = "L e v e l 0 9", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0.4, y = -0.1, parent = self.levels_fin_menu)

        level10_button = Button(text = "L e v e l 1 0", color = color.black, scale_y = 0.1, scale_x = 0.3, x = 0, y = -0.3, parent = self.levels_fin_menu)
        back_fin_button = Button(text = "< - B a c k", color = color.gray, scale_y = 0.05, scale_x = 0.2, y = -0.4, parent = self.levels_fin_menu)

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
        back_fin_button.on_click = Func(back_fin)