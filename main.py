import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys
def main():
    pygame.init()
    print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroid_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers=(updatable_group, drawable_group, shot_group)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000
        updatable_group.update(dt)
        for asteroid in asteroid_group:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit(0)
        for asteroid in asteroid_group:
            for shot in shot_group:
                if asteroid.check_collisions(shot):
                    asteroid.split(asteroid_group)
                    shot.kill()


if __name__ == "__main__":
    main()
