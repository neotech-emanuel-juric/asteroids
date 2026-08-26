import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock() # new clock object for fps
    dt = 0.0 # Delta

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = gameClock.tick(60) / 1000 # tick() method returns the amount of time that has passed since the last time it was called: the delta time


if __name__ == "__main__":
    main()
