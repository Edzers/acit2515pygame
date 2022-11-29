import pygame
from components.sprite import Sprite


class Mainchar(Sprite):
    def __init__(self):
        super().__init__("graphics/idle1.png")
        self.rect.x = 100
        self.rect.y = 500
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.player_index = 0

    def default(self):
        self.image = pygame.image.load("graphics/idle1.png")
        return self.image

    def idle2(self):
        self.image = pygame.image.load("graphics/idle2.png")
        return self.image

    def animation_state(self):
        self.sprite_list = ["default", "idle2"]
        self.player_index += 0.1

        if self.player_index >= len(self.sprite_list):
            self.player_index = 0
            self.image = self.sprite_list[int(self.player_index)]()
            print(self.image)  

    def update(self):
        self.animation_state()
                  
