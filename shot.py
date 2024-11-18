import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        for container in Shot.containers:
            container.add(self)

    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
