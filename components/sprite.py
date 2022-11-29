import pygame

class Sprite(pygame.sprite.Sprite):
    #Class to import sprites
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()