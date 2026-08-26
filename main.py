import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock() # new clock object for fps
    dt = 0.0 # Delta
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen) # draw the player here - it is important to fill in first, then draw sprite(s), then .flip()
        pygame.display.flip()
        dt = gameClock.tick(60) / 1000 # tick() method returns the amount of time that has passed since the last time it was called: the delta time


if __name__ == "__main__":
    main()
