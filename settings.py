import pygame
from screens.mainscreen import Basescreen
from screens.game_over_screen import GameOver
from screens.welcomescreen import WelcomeScreen

class Game:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("ShootandRun")
        
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False
                    
        
       

if __name__ == "__main__":
    settings = Game()
    settings.run()