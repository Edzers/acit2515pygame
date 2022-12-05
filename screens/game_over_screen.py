import pygame
from screens.mainscreen import Basescreen

class GameOver(Basescreen):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.titletext = self.test_font.render("You Lose!", True, (255, 255, 255))

    def draw(self):
        #Draw the text
        self.window.fill((64, 64, 64))
        self.window.blit(self.titletext, (400, 180))


    def update(self):
        pass

    def manage_event(self, event):
        #Check to see if the game is started
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "gameover"
            self.running = False



            