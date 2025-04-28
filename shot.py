from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):

    def __init__(self, x, y, velocty):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocty
    
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=(self.position), radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt