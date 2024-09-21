import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update the player's state
        player.update(dt)
        
        # Clear the screen
        screen.fill("black")

        # Draw the player
        player.draw(screen)

        # Swap the buffers to display the new frame
        pygame.display.flip()

        # limit the framrate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()