import pygame
from components.sprite import Sprite

class Knuckles(Sprite):
    #Class for the main enemy obstacle

    def __init__(self):
        super().__init__("graphics/knuckles.png")
        self.rect.x = 800
        self.rect.y = 580
        self.image = pygame.transform.scale(self.image, (150,150))


   


