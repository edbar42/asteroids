from typing import Tuple

import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    containers: Tuple[pygame.sprite.Group, ...] = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)

    def draw(self, screen):
        return pygame.draw.circle(
            screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt
