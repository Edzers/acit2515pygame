import pygame

class Screens:
    
    def __init__(self, window):
        self.window = window
        self.next_screen = False
        
        
    def run(self):
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
                    
        