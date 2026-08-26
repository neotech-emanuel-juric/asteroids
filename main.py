import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock() # new clock object for fps
    dt = 0.0 # Delta

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # Add Player Class to updatable and drawable pygame group, before an instance of Player exists
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen) # draw the sprite(s) here - it is important to fill in first, then draw sprite(s), then .flip()
        pygame.display.flip()
        dt = gameClock.tick(60) / 1000 # tick() method returns the amount of time that has passed since the last time it was called: the delta time


if __name__ == "__main__":
    main()
