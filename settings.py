import pygame

def main() -> None:
    pygame.init()
    screen_height = 100
    screen_width = 100
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    
    

if __name__ == "__main__":
    main()