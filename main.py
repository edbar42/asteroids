import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    playerObj = Player(x, y)
    dt = 0
    updatable = pygame.sprite.Group(playerObj)
    drawable = pygame.sprite.Group(playerObj)
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0
        screen.fill(000000)
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(playerObj):
                print("Game over!")
                pygame.quit()
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    main()
