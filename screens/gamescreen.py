import pygame
from screens.mainscreen import Basescreen
from components.knuckles import Knuckles
from components.mainchar import Mainchar

class GameScreen(Basescreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Add sprites to a group
        self.knuckles = Knuckles()
        self.mainchar = Mainchar()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.knuckles)
        self.sprites.add(self.mainchar)
        self.points = 0
    
    # Update sprites and collision
    def update(self):
        self.sprites.update()
        self.points += 1
        if self.mainchar.rect.colliderect(self.knuckles.rect):
            self.next_screen = "gameover"
            self.running = False
            self.score.add_score(self.points)


    def draw(self):
        #Draw the sprites
        self.window.fill((255, 255, 255))
        #Blit background, and score
        self.window.blit(self.sky_surface1, (0,0))
        self.window.blit(self.ground_surface1, (0,300))
        self.sprites.draw(self.window)
        self.score_text = self.test_font.render(
            f"SCORE: {self.points}", True, (255, 255, 255))
        self.score_text.get_rect(center=(self.window.get_width() / 2, 200))
        self.window.blit(self.score_text, (50, 50))
    
    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"


