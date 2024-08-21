import pygame
from constants import *
from player import Player

clock = pygame.time.Clock()
dt = 0

# Set game groups
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updateable, drawable)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Set frame rate to 60
        dt = clock.tick(60) / 1000

        # Create black screen 
        screen.fill((0, 0, 0))
        
        for sprite in updateable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()