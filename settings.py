import pygame

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
                    
        
       

if __name__ == "__main__":
    settings = Game()
    settings.run()