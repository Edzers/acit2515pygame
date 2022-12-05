import pygame
class Mainchar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Setup base values for sprite and needed spritesheet 
        self.x_vel = 0
        self.y_vel = 0
        self.state = 'idle'
        self.player_vel = 5
        self.frog_index = 0
        self.default = (300, 720)

        self.BLACK = (0, 0, 0)

        # Load mainchar images for idle
        frogidle1 = pygame.image.load('graphics/NinjaFrog/idle1frog.png').convert_alpha()
        frogidle2 = pygame.image.load('graphics/NinjaFrog/idle2frog.png').convert_alpha()
        frogidle3 = pygame.image.load('graphics/NinjaFrog/idle3frog.png').convert_alpha()
        frogidle4 = pygame.image.load('graphics/NinjaFrog/idle4frog.png').convert_alpha()
        frogidle5 = pygame.image.load('graphics/NinjaFrog/idle5frog.png').convert_alpha()
        frogidle6 = pygame.image.load('graphics/NinjaFrog/idle6frog.png').convert_alpha()
        frogidle7 = pygame.image.load('graphics/NinjaFrog/idle7frog.png').convert_alpha()
        frogidle8 = pygame.image.load('graphics/NinjaFrog/idle8frog.png').convert_alpha()
        frogidle9 = pygame.image.load('graphics/NinjaFrog/idle9frog.png').convert_alpha()
        frogidle10 = pygame.image.load('graphics/NinjaFrog/idle10frog.png').convert_alpha()
        frogidle11 = pygame.image.load('graphics/NinjaFrog/idle11frog.png').convert_alpha()

        self.frog_jump = pygame.image.load('graphics/NinjaFrog/jump.png').convert_alpha()
        self.frog_jump = pygame.transform.scale(self.frog_jump, (self.frog_jump.get_width()*2, self.frog_jump.get_height()*2))

        # Put in a list
        self.frogidle = [frogidle1, frogidle2, frogidle3, frogidle4, frogidle5, frogidle6, frogidle7,
        frogidle8, frogidle9, frogidle10, frogidle11]

        self.frogidle = [pygame.transform.scale(frog, (frog.get_width()*2, frog.get_height()*2)) for frog in self.frogidle]

        # Load mainchar images for run
        frogrun1 = pygame.image.load('graphics/NinjaFrog/run1.png').convert_alpha()
        frogrun2 = pygame.image.load('graphics/NinjaFrog/run2.png').convert_alpha()
        frogrun3 = pygame.image.load('graphics/NinjaFrog/run3.png').convert_alpha()
        frogrun4 = pygame.image.load('graphics/NinjaFrog/run4.png').convert_alpha()
        frogrun5 = pygame.image.load('graphics/NinjaFrog/run5.png').convert_alpha()
        frogrun6 = pygame.image.load('graphics/NinjaFrog/run6.png').convert_alpha()
        frogrun7 = pygame.image.load('graphics/NinjaFrog/run7.png').convert_alpha()
        frogrun8 = pygame.image.load('graphics/NinjaFrog/run8.png').convert_alpha()
        frogrun9 = pygame.image.load('graphics/NinjaFrog/run9.png').convert_alpha()
        frogrun10 = pygame.image.load('graphics/NinjaFrog/run10.png').convert_alpha()
        frogrun11 = pygame.image.load('graphics/NinjaFrog/run11.png').convert_alpha()
        frogrun12 = pygame.image.load('graphics/NinjaFrog/run12.png').convert_alpha()

        self.frogrun = [frogrun1, frogrun2, frogrun3, frogrun4, frogrun5, frogrun6, 
        frogrun7, frogrun8, frogrun9, frogrun10, frogrun11, frogrun12]

        self.frogrun= [pygame.transform.scale(frog, (frog.get_width()*2, frog.get_height()*2)) for frog in self.frogrun]

        # Get image and rect
        self.image = self.frogidle[self.frog_index]
        self.rect = self.image.get_rect(bottomleft=self.default)
       
    #Set state of player
    def set_state(self):
        self.state = 'idle'
        if self.player_vel > 0:
            self.state = 'moving_right'
        elif self.player_vel < 0:
            self.state = 'moving_left'
        
    # Gravity
    def model_gravity(self):
        self.gravity += 1 
        self.rect.y += self.gravity
        if self.rect.bottom >= 720:
            self.rect.bottom = 720

    # Animate the various states
    def animate(self):
        if self.state == 'idle':
            self.frog_index += 0.25
            if self.frog_index >= len(self.frogidle):
                self.frog_index = 0
            self.image = self.frogidle[int(self.frog_index)]
        else:
            if self.state == 'moving_right':
                self.frog_index += 0.25
                if self.frog_index >= len(self.frogrun):
                    self.frog_index = 0
                self.image = self.frogrun[int(self.frog_index)]
            if self.state == 'moving_left':
                self.frog_index += 0.25
                if self.frog_index >= len(self.frogrun):
                    self.frog_index = 0
                self.image = pygame.transform.flip(self.frogrun[int(self.frog_index)], flip_x = 1, flip_y = 0)
            if self.rect.bottom < 720:
                self.image = self.frog_jump
    
    # Movement function
    def movement(self):
        keystroke = pygame.key.get_pressed()

        self.player_vel = 0
        if keystroke[pygame.K_a]:
            self.player_vel = -3.5
        if keystroke[pygame.K_d]:
            self.player_vel = 4
        if keystroke[pygame.K_SPACE] and self.rect.bottom == 720:
            self.gravity = -20

        self.rect.x += self.player_vel
        

    def update(self):
        self.set_state()
        self.movement()
        self.model_gravity()
        self.animate()

