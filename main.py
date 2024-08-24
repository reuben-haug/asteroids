import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

clock = pygame.time.Clock()
dt = 0

# Set game groups
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid = pygame.sprite.Group()

# Set containers for each class
Player.containers = (updateable, drawable)
Asteroid.containers = (updateable, drawable, asteroid)
AsteroidField.containers = (updateable)

# Create game objects
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

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
        
        # Update and draw game objects
        for sprite in updateable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        # Update display
        pygame.display.flip()

if __name__ == "__main__":
    main()