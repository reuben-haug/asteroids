import pygame
from constants import *

clock = pygame.time.Clock()
dt = 0

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
            
        screen.fill((0, 0, 0))
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()