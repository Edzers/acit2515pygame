import pygame
from components.sprite import Sprite


class Mainchar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("graphics/idle1.png")
        self.rect.x = 100
        self.rect.y = 500
        sprite_list = [
        pygame.image.load("graphics/idle1.png"),
        pygame.image.load("graphics/idle2.png"),
        pygame.image.load("graphics/idle3.png"),
        pygame.image.load("graphics/idle4.png")
        ]
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.player_index = 0

    def animation_state(self):
        pass
