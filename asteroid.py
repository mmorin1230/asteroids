from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=(self.position), radius=self.radius, width=2)
    
    def split(self, asteroid_group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        rand_angle1 = self.velocity.rotate(angle)
        rand_angle2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = rand_angle1 * 1.2
        asteroid1.add(asteroid_group)

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = rand_angle2 * 1.2
        asteroid2.add(asteroid_group)

    def update(self, dt):
        self.position += self.velocity * dt