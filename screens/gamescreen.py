import pygame
from screens.mainscreen import Basescreen
from components.knuckles import Knuckles

class GameScreen(Basescreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Add sprites to a group
        self.sprites = pygame.sprite.Group()
        self.knuckles = Knuckles()

    def update(self):
        self.sprites.update()


    def draw(self):
        #Draw the sprites
        self.sprites.draw(self.window)
        self.window.fill((255, 255, 255))
        #Blit background
        self.window.blit(self.sky_surface1, (0,0))
        self.window.blit(self.ground_surface1, (0,300))

    def manage_event(self, event):
        pass


