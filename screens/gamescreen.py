import pygame
from screens.mainscreen import Basescreen
from components.knuckles import Knuckles

class GameScreen(Basescreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sprites = pygame.sprite.Group()
        self.knuckles = Knuckles()


