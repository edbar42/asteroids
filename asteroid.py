import random
from typing import Tuple

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers: Tuple[pygame.sprite.Group, ...] = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)

    def draw(self, screen):
        return pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = v1 * 1.2
        ast2.velocity = v2 * 1.2
