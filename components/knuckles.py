import pygame
class Knuckles(pygame.sprite.Sprite):
    #Class for the main enemy obstacle

    def __init__(self):
        super().__init__()
        knuckle = pygame.image.load("graphics/knuckles.png").convert_alpha()
        knuckle = pygame.transform.scale(knuckle, (110,110))
        self.image = knuckle
        self.rect = self.image.get_rect(midbottom=(800, 730))       

    
    def update(self):
        self.rect.x -= 6
        if self.rect.x < - 100: 
            self.rect.x = 950




   


