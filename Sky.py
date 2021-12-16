from ursina import *

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture = "./assets/Sky", 
            double_sided = True, 
            scale = 10000
            )

class Song(Audio):
    def __init__(self):
        super().__init__(
            sound_file_name = "./assets/tabletop.wav",
            volume = 1,
            auto_play = True,
            loop = True
            )

        def pause():
            self.is_pause = True
            self.song.pause()

        def play():
            self.is_play = True
            self.song.play()

        def resume():
            self.is_resume = True
            self.song.resume()

class Vic(Audio):
    def __init__(self):
        super().__init__(
            sound_file_name = "./assets/Victory sound effect.wav",
            volume = 2,
            auto_play = True,
            loop = False
            )

        def pause():
            self.is_pause = True
            self.vic.pause()

        def play():
            self.is_play = True
            self.vic.play()

        def resume():
            self.is_resume = True
            self.vic.resume()

class Die(Audio):
    def __init__(self):
        super().__init__(
            sound_file_name = "./assets/youdiedsound.wav",
            volume = 0.3,
            auto_play = True,
            loop = False
            )

        def pause():
            self.is_pause = True
            self.die.pause()

        def play():
            self.is_play = True
            self.die.play()

        def resume():
            self.is_resume = True
            self.die.resume()







