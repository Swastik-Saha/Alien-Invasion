from pygame import mixer


class SoundEffects:

    def __init__(self):
        self.shoot_sound = "sound/alien_shoot.mp3"

    mixer.init()

    def play_alien_shoot_sound(self):
        mixer.music.load(self.shoot_sound)
        mixer.music.play()
