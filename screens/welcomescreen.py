import pygame
from screens.mainscreen import Basescreen

class WelcomeScreen(Basescreen):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Setup text
        self.titletext = self.test_font.render("Welcome to the game", True, (255, 255, 255))
        self.gamestarttext= self.test_font.render("Click to start", True, (255, 255, 255))
        
    def draw(self):
        #Draw the text
        self.window.blit(self.titletext, (320, 180))
        self.window.blit(self.gamestarttext, (370, 420))

    def manage_event(self, event):
        #Check to see if the game is started
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "main"
            self.running = False


    def update(self):
        pass
