import pygame

class Basescreen:
    
    def __init__(self, window):
        pygame.font.init()

        #Set window
        self.window = window
        self.next_screen = False

        self.sky_surface = pygame.image.load("graphics/sky.jpg")
        self.ground_surface = pygame.image.load()

        
        
    def run(self):
        #Base game loop
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(60)
            self.update()
            self.draw()
            pygame.display.update()
            
            for event in pygame.get.event():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                    
        