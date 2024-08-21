import pygame
from constants import *
from player import Player

clock = pygame.time.Clock()
dt = 0

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Set frame rate to 60
        dt = clock.tick(60) / 1000
        
        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()