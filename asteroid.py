from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.radius)
    
    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt # Get velocity from parent class