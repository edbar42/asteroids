import pygame

from circleshape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_SHOT_COOLDOWN, PLAYER_SHOT_SPEED,
                       PLAYER_SPEED, PLAYER_TURN_SPEED)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.shots = pygame.sprite.Group()
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        mult_factor = self.radius / 1.5
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * mult_factor
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return (a, b, c)

    def draw(self, screen):
        return pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 3)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, self.rotation)
            direction = pygame.Vector2(0, 1)
            direction = direction.rotate(self.rotation)
            shot.velocity = direction * PLAYER_SHOT_SPEED
            self.timer = PLAYER_SHOT_COOLDOWN
