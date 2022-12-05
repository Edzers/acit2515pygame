import pygame
from components.score import Score

class Basescreen:
    
    def __init__(self, window):
        pygame.font.init()

        #Set window
        self.window = window
        self.next_screen = False

        #Initialize score
        self.score = Score()

        #Load background images
        self.sky_surface = pygame.image.load("graphics/sky.jpg")
        self.ground_surface = pygame.image.load("graphics/ground.png")
        self.sky_surface1 = pygame.transform.scale(self.sky_surface, (1000,800))
        self.ground_surface1 = pygame.transform.scale(self.ground_surface, (1000, 800))

        #Set up fonts
        self.test_font = pygame.font.Font(None, 50)

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(60)
            self.update()
            self.draw()
            pygame.display.update()

            # Main event loop for the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
                    self.next_screen = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False
                    

                self.manage_event(event)
        