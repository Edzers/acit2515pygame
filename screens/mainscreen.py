import pygame

class Basescreen:
    
    def __init__(self, window):
        pygame.font.init()

        #Set window
        self.window = window
        self.next_screen = False

        #Load background images
        self.sky_surface = pygame.image.load("graphics/sky.jpg")
        self.ground_surface = pygame.image.load("graphics/ground.png")

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
            for event in pygame.get.event():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False
                    
        