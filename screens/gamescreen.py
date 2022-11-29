import pygame
from screens.mainscreen import Basescreen
from components.knuckles import Knuckles
from components.mainchar import Mainchar

class GameScreen(Basescreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Add sprites to a group
        self.knuckles = Knuckles()
        self.mainchar = Mainchar()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.knuckles)
        self.sprites.add(self.mainchar)
    
    def update(self):
        self.sprites.update()

    def draw(self):
        #Draw the sprites
        self.window.fill((255, 255, 255))
        #Blit background
        self.window.blit(self.sky_surface1, (0,0))
        self.window.blit(self.ground_surface1, (0,300))
        self.sprites.draw(self.window)


    def manage_event(self, event):
        pass


