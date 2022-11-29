import pygame
from screens.mainscreen import Basescreen

class WelcomeScreen(Basescreen):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Setup text
        self.titletext = self.test_font.render("Welcome to the game", True, (255, 255, 255))
        
    def draw(self):
        #Draw the text
        self.window.blit(self.titletext, (330, 180))

    def check_state(self, event):
        #Check to see if the game is started
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "main"
            self.running = False


    def update(self):
        pass
