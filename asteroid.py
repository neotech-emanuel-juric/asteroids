from circleshape import CircleShape
import pygame
import random
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.radius)
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            ran_angle = random.uniform(20.0, 50.0)
            first_movement = self.velocity.rotate(ran_angle)
            second_movement = self.velocity.rotate(-ran_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = first_movement * 1.2
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = second_movement * 1.2

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt # Get velocity from parent class

