import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update the objects state
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        # Clear the screen
        screen.fill("black")

        # Draw the objects
        for obj in drawable:
            obj.draw(screen)

        # Swap the buffers to display the new frame
        pygame.display.flip()

        # limit the framrate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()