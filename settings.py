import pygame
from screens.mainscreen import Basescreen
from screens.gamescreen import GameScreen
from screens.game_over_screen import GameOver
from screens.welcomescreen import WelcomeScreen

class Game:
    
    def __init__(self):
        self.window = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("ShootandRun")
        
    def run(self):
        screens = {
            "welcome": WelcomeScreen,
            "main": GameScreen,
            "gameover": GameOver,
        }
        running = True
        current_screen = "welcome"

        while running:
            #Get screen class
            screen_state = screens.get(current_screen)

            #Create new screen object
            screen = screen_state(self.window)

            screen.run()

            #Next screen if false
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen

if __name__ == "__main__":
    maingame = Game()
    maingame.run()