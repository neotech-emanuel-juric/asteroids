from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_RIGHT_KEY, PLAYER_LEFT_KEY, PLAYER_FORWARD_KEY, PLAYER_BACKWARDS_KEY
from circleshape import CircleShape
import pygame

class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float = PLAYER_RADIUS) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.rotation = 0

        super().__init__(self.x, self.y, self.radius)

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[PLAYER_LEFT_KEY]:
            self.rotate(-dt) # Inverse/Negative delta time for moving backwards or to the left
        if keys[PLAYER_RIGHT_KEY]:
            self.rotate(dt)
        if keys[PLAYER_BACKWARDS_KEY]:
            self.move(-dt)
        if keys[PLAYER_FORWARD_KEY]:
            self.move(dt)